#!/usr/bin/env python
# -*- coding: utf-8 -*-


def insert_text_output_pdfrw(pdf_file_path, insert_text):
    """
    既存のPDFファイルに文字を挿入し、別名で出力します
    :param pdf_file_path:       既存のPDFファイルパス
    :param insert_text:         挿入するテキスト
    :return:
    """
    from pdfrw import PdfReader
    from pdfrw.buildxobj import pagexobj
    from pdfrw.toreportlab import makerl
    from reportlab.pdfgen import canvas
    from reportlab.pdfbase.cidfonts import UnicodeCIDFont
    from reportlab.pdfbase import pdfmetrics
    from reportlab.lib.units import mm

    # 出力名
    output_name = "pdfrw.pdf"
    # PDF新規作成
    cc = canvas.Canvas(output_name)

    # フォントの設定
    font_name = "HeiseiKakuGo-W5"
    pdfmetrics.registerFont(UnicodeCIDFont(font_name))
    cc.setFont(font_name, 16)

    # 既存ページ読み込み
    page = PdfReader(pdf_file_path, decompress=False).pages
    # 1ページ目をオブジェクトに
    pp = pagexobj(page[0])
    cc.doForm(makerl(cc, pp))

    # 挿入位置(mm指定)
    target_x, target_y = 10*mm, 10*mm
    # 文字列挿入
    cc.drawString(target_x, target_y, insert_text)
    cc.showPage()
    # 保存
    cc.save()


def insert_text_output_pdf_PyPDF2(pdf_file_path, insert_text):
    """
    既存のPDFファイルに文字を挿入し、別名で出力します
    :param pdf_file_path:       既存のPDFファイルパス
    :param insert_text:         挿入するテキスト
    :return:
    """
    from PyPDF2 import PdfFileWriter, PdfFileReader
    from io import BytesIO
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import mm

    buffer = BytesIO()
    # PDF新規作成
    p = canvas.Canvas(buffer, pagesize=A4)
    # 挿入位置(mm指定)
    target_x, target_y = 10*mm, 10*mm
    p.drawString(target_x, target_y, insert_text)
    p.showPage()
    p.save()

    # move to the beginning of the StringIO buffer
    buffer.seek(0)
    new_pdf = PdfFileReader(buffer)
    # read your existing PDF
    existing_pdf = PdfFileReader(open(pdf_file_path, 'rb'), strict=False)
    output = PdfFileWriter()
    # 既存PDFの1ページ目を読み取り
    page = existing_pdf.getPage(0)
    # 新規PDFにマージ
    page.mergePage(new_pdf.getPage(0))

    output.addPage(page)
    # 出力名
    output_name = "PyPDF2.pdf"
    output_stream = open(output_name, 'wb')
    output.write(output_stream)
    output_stream.close()


def insert_text_output_pdf_fitz(pdf_file_path, insert_text):
    """
    既存のPDFファイルに文字を挿入し、別名で出力します
    :param pdf_file_path:       既存のPDFファイルパス
    :param insert_text:         挿入するテキスト
    :return:
    """
    import fitz

    # 既存PDFの読み取り
    reader = fitz.open(pdf_file_path)
    # 新規PDFの作成
    writer = fitz.open()
    # 既存PDFの1ページ目を新規PDFに流し込む
    writer.insertPDF(reader, from_page=0, to_page=0)
    # 既存PDFの1ページを読み込む
    page = writer.loadPage(0)
    # 挿入位置(mmをptsに変えて指定)
    target_x, target_y = mm_to_pts(10), mm_to_pts(10)
    p = fitz.Point(target_x, target_y)  # start point of 1st line
    rc = page.insertText(p,  # bottom-left of 1st char
                         insert_text,  # the text (honors '\n')
                         fontname="helv",  # the default font
                         fontsize=16,  # the default font size
                         rotate=0,  # also available: 90, 180, 270
                         )
    # 出力名
    output_name = "PyMuPDF.pdf"
    writer.save(output_name)


def pts_to_mm(pts) -> float:
    """
    ptsからmmに変換します
    :param pts:
    :return:
    """
    return float(pts) * 0.352778


def mm_to_pts(mm) -> float:
    """
    mmからptsに変換します
    :param mm:
    :return:
    """
    return float(mm) / 0.352778


if __name__ == '__main__':
    file_path = "dummy.pdf"
    insert_text_output_pdfrw(file_path, "pdfrwだお")
    insert_text_output_pdf_PyPDF2(file_path, "PyPDF2だお")
    insert_text_output_pdf_fitz(file_path, "PyMuPDFだお")

