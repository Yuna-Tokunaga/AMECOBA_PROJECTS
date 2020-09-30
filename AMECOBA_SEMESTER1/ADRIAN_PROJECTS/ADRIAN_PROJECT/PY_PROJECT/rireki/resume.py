# -*- coding: utf-8 -*-
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.lib.pagesizes import A4, portrait
from reportlab.platypus import Table, TableStyle
from reportlab.lib.units import mm
from reportlab.lib import colors

# 初期設定
def make(filename="resume"): # ファイル名
    pdf_canvas = set_info(filename) # キャンバス名
    print_string(pdf_canvas)
    pdf_canvas.save() # 保存

def set_info(filename):
    pdf_canvas = canvas.Canvas("./{0}.pdf".format(filename)) # 保存先
    pdf_canvas.setAuthor("") # 作者
    pdf_canvas.setTitle("") # 表題
    pdf_canvas.setSubject("") # 件名
    return pdf_canvas

#履歴書フォーマット作成
def print_string(pdf_canvas):
    pdfmetrics.registerFont(UnicodeCIDFont('HeiseiKakuGo-W5')) # フォント
    width, height = A4 # 用紙サイズ
 # (1)履歴書 タイトル
    font_size = 24 # フォントサイズ
    pdf_canvas.setFont('HeiseiKakuGo-W5', font_size)
    pdf_canvas.drawString(60, 770, '履  歴  書') # 書き出し(横位置, 縦位置, 文字)

    # (2)作成日
    font_size = 10
    pdf_canvas.setFont('HeiseiKakuGo-W5', font_size)
    pdf_canvas.drawString(285, 770,  '    年         月         日現在')

    # (3)証明写真
    # tableを作成
    data = [
            ['    証明写真'],
        ]
    table = Table(data, colWidths=30*mm, rowHeights=40*mm) # tableの大きさ
    table.setStyle(TableStyle([                              # tableの装飾
            ('FONT', (0, 0), (0, 0), 'HeiseiKakuGo-W5', 12), # フォントサイズ
            ('BOX', (0, 0), (0, 0), 1, colors.black),        # 罫線
            ('VALIGN', (0, 0), (0, 0), 'MIDDLE'),            # フォント位置
        ]))
    table.wrapOn(pdf_canvas, 145*mm, 235*mm) # table位置
    table.drawOn(pdf_canvas, 145*mm, 235*mm)
# (4) プロフィール
    data = [
            ['ふりがな','   男  ・  女'],  
            ['氏名',''],
            ['生年月日　　　　　　　　　　                          年　　　月　　　日生　（満　　　歳）',''],    
        ]
    table = Table(data, colWidths=(100*mm,20*mm), rowHeights=(7*mm, 20*mm, 7*mm))
    table.setStyle(TableStyle([
            ('FONT', (0, 0), (1, 2), 'HeiseiKakuGo-W5', 8),
            ('BOX', (0, 0), (1, 2), 1, colors.black),
            ('INNERGRID', (0, 0), (1, 2), 1, colors.black),
            ('SPAN',(0, 2), (1, 2)),
            ('SPAN',(1, 0), (1, 1)),
            ('VALIGN', (0, 0), (1, 2), 'MIDDLE'),
            ('VALIGN', (0, 1), (0, 1),'TOP'),
        ]))
    table.wrapOn(pdf_canvas, 20*mm, 232*mm)
    table.drawOn(pdf_canvas, 20*mm, 232*mm)

    # (5)住所
    data = [
            ['ふりがな', '電話'],
            ['連絡先（〒　　　ー　　　　）', 'E-mail'],
            ['ふりがな', '電話'],
            ['連絡先（〒　　　ー　　　　）', 'E-mail'],
        ]
    table = Table(data, colWidths=(120*mm, 40*mm), rowHeights=(7*mm,20*mm,7*mm,20*mm))
    table.setStyle(TableStyle([
            ('FONT', (0, 0), (1, 3), 'HeiseiKakuGo-W5', 9),
            ('BOX', (0, 0), (1, 3), 1, colors.black),
            ('INNERGRID', (0, 0), (1, 3), 1, colors.black),
            ('VALIGN', (0, 0), (1, 2), 'MIDDLE'),
            ('VALIGN', (0, 1), (1, 1), 'TOP'),
            ('VALIGN', (0, 3), (1, 3), 'TOP'),
        ]))
    table.wrapOn(pdf_canvas, 20*mm, 178*mm)
    table.drawOn(pdf_canvas, 20*mm, 178*mm)

    # (6)学歴・職歴
    data = [
            ['        年', '   月', '                                            学歴・職歴'],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
    table = Table(data, colWidths=(25*mm, 14*mm, 121*mm), rowHeights=7.5*mm)
    table.setStyle(TableStyle([
            ('FONT', (0, 0), (-1, -1), 'HeiseiKakuGo-W5', 11),
            ('BOX', (0, 0), (-1, -1), 1, colors.black),
            ('INNERGRID', (0, 0), (-1, -1), 1, colors.black),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ]))
    table.wrapOn(pdf_canvas, 20*mm, 20*mm)
    table.drawOn(pdf_canvas, 20*mm, 20*mm)

    # 1枚目終了
    pdf_canvas.showPage()

 # (7)学歴・職歴、免許・資格
    data = [ 
            ['        年', '   月', '                                            学歴・職歴'],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            ['        年', '   月', '                                            免許・資格'],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
        ]
    table = Table(data, colWidths=(25*mm, 14*mm, 121*mm), rowHeights=7.5*mm)
    table.setStyle(TableStyle([
            ('FONT', (0, 0), (-1, -1), 'HeiseiKakuGo-W5', 11),
            ('BOX', (0, 0), (-1, -1), 1, colors.black),
            ('INNERGRID', (0, 0), (-1, -1), 1, colors.black),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ]))
    table.wrapOn(pdf_canvas, 20*mm, 132*mm)
    table.drawOn(pdf_canvas, 20*mm, 132*mm)

    # (8)そのほか
    data = [
            ['志望の動機、自己PR、趣味、特技など','通勤時間',''],
            ['','                        約　　　　時間　　　　分',''],
            ['','扶養家族（配偶者を除く）',''],
            ['','                              　　　　    　　　　人',''],
            ['','配偶者','配偶者の扶養義務'],
            ['','       有    ・    無','       有    ・    無'],
            ['本人希望記入欄（特に待遇・職種・勤務時間・その他についての希望などがあれば記入）','',''],
            ['','','']

        ]
    table = Table(data, colWidths=(90*mm, 35*mm, 35*mm), rowHeights=(8*mm, 10*mm, 8*mm, 10*mm, 8*mm, 10*mm, 8*mm, 50*mm))
    table.setStyle(TableStyle([
            ('FONT', (0, 0), (2, 7), 'HeiseiKakuGo-W5', 10),
            ('BOX', (0, 0), (2, 7), 1, colors.black),
            ('LINEBEFORE', (1, 0), (1, 5), 1, colors.black),
            ('LINEBEFORE', (2, 4), (2, 5), 1, colors.black),
            ('LINEABOVE', (1, 2), (2, 2), 1, colors.black),
            ('LINEABOVE', (1, 4), (2, 4), 1, colors.black),
            ('LINEABOVE', (0, 6), (2, 6), 1, colors.black),
            ('LINEABOVE', (0, 7), (2, 7), 1, colors.black),
            ('VALIGN', (0, 0), (2, 5), 'TOP'),
            ('VALIGN', (0, 6), (2, 6), 'MIDDLE'),
        ]))
    table.wrapOn(pdf_canvas, 20*mm, 20*mm)
    table.drawOn(pdf_canvas, 20*mm, 20*mm)

    # 2枚目終了
    pdf_canvas.showPage()


# 作成
if __name__ == '__main__':
    make()
