# pdf2images
pdf2images is a script to convert one PDF to images

usage: pdf2images_app.py [-h] --file pdf_path [--out out_dir]
                         [--loglevel LEVEL]

Convert a PDF to images

optional arguments:
  -h, --help        show this help message and exit
  --file pdf_path   the path to the pdf file
  --out out_dir     path to output directory
  --loglevel LEVEL  Loglevel : ERROR, DISABLED or DEBUG


**Result :**
_**in case of success :**_
`{"status": "success", "page_count": 10}`

_**in case of conversion error :**_
`{"status": "convert_error", "error": "Unable to get page count. I/O Error: Couldn't open file '/afb/a.pdf': No such file or directory.\n"}
`

**_in case of resize error :_**
`{"status": "resize_error", "error": "[Errno 13] Permission denied: '/sample.pdf-resize-0.jpg'"}`