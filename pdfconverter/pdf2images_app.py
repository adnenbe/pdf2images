#!/usr/bin/python

import os
import sys
import json
import logging

from datetime import datetime
from pdf2image import convert_from_path
from PIL import Image


def main(pdf_file, out, loglevel):

    logger = logging.getLogger('PDF2IMG')
    if loglevel == 'ERROR':
        level = logging.ERROR
    elif loglevel == 'DEBUG':
        level = logging.DEBUG
    elif loglevel == 'DISABLED':
        level = logging.CRITICAL
        logging.getLogger().disabled = True
    else:
        level = logging.CRITICAL
        logging.getLogger().disabled = True

    logging.basicConfig(level=level)

    logger.debug("PDF file to convert  = %s" % pdf_file)
    if out is None:
        out = os.path.dirname(pdf_file)
    logger.debug ("Output folder  = %s" % (out))

    size = 795, 1030

    # To convert single page
    logger.debug("Start Convertion ...")

    step1 = datetime.now()

    try:
        pages = convert_from_path(pdf_file)
    except Exception as e:
        res = {"status": "convert_error", "error": str(e)}
        print json.dumps(res)
        exit(0)

    step2 = datetime.now()
    tt = (step2 - step1).seconds + float((step2 - step1).microseconds) / 1000000

    logger.debug("Convert Time  = %f seconds" % (tt))

    logger.debug("Start converting image resolution ...")
    i = 0
    for page in pages:
        try:
            im_resize = page.resize(size, Image.ANTIALIAS)
            im_resize.save(out + os.path.basename(pdf_file) + '-resize-' + str(i) + '.jpg', 'JPEG')
            i = i + 1
        except Exception as e:
            res = {"status": "resize_error", "error": str(e)}
            print json.dumps(res)
            exit(0)
    end = datetime.now()
    tt = (end - step2).seconds + float((end - step2).microseconds) / 1000000
    logger.debug("saving with image resolution %s Time  = %f seconds" % (str(size), tt))
    tt = (end - step1).seconds + float((end - step1).microseconds) / 1000000
    logger.debug("Overall Time  = %f seconds" % (tt))
    logger.debug("converted files  = %d " % i)

    res = {"status": "success", "page_count": i}
    print json.dumps(res)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Convert a PDF to images')
    parser.add_argument('--file', metavar='pdf_path', required=True,
                        help='the path to the pdf file')
    parser.add_argument('--out', metavar='out_dir', required=False,
                        help='path to output directory')
    parser.add_argument('--loglevel', metavar='LEVEL', required=False,
                        help='Loglevel : ERROR, DISABLED or DEBUG')

    args = parser.parse_args()
    main(pdf_file=args.file, out=args.out, loglevel=args.loglevel)

