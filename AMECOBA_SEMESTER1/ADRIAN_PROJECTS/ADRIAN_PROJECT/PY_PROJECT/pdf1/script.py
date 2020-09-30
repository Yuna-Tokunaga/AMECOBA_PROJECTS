#! /usr/bin/python
#
#   pdf_gen.py
#
#                       Oct/02/2018
#
# -------------------------------------------------------------------------
import sys
from reportlab.pdfgen import canvas
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfbase import pdfmetrics

# -------------------------------------------------------------------------
def draw01_proc(cc):
    cc.drawString(100,700,"こんにちは")
    cc.drawString(100,600,"本日は晴天なり")
    cc.drawString(100,500,"Good Afternoon")
    cc.drawString(100,400,"Hello World")
#
# -------------------------------------------------------------------------
sys.stderr.write ("*** 開始 ***\n")
#
file_pdf = "out01.pdf"
cc = canvas.Canvas(file_pdf)
fontname_g = "HeiseiKakuGo-W5"
pdfmetrics.registerFont (UnicodeCIDFont (fontname_g))
cc.setFont(fontname_g,16)

draw01_proc(cc)
cc.showPage()
cc.save()
#
sys.stderr.write ("*** 終了 ***\n")
# -------------------------------------------------------------------------