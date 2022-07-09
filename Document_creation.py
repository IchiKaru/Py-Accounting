import time
from docx import *
from docx.enum.style import *
from docx.shared import *
from docx.oxml.ns import qn
from docx.enum.section import WD_SECTION

document = Document()
sections = document.sections
for section in sections:
    section.top_margin = Inches(0.5)
    section.bottom_margin = Inches(0.5)
    section.left_margin = Inches(1)
    section.right_margin = Inches(1)

section = document.sections[0]

sectPR =  section._sectPr
cols = sectPR.xpath('./w:cols')[0]

cols.set(qn('w:num'), '1')

document.add_heading('Balance Sheet', 0)
s = document.sections[0]
s.start_type = WD_SECTION


global content
content = 'Hello, thank you for using Py-accounting software. You May Delete this Message.'

def createdocx():
    cols.set(qn('w:num'), '4')
    p = document.add_paragraph(content)
    p.style = document.styles.add_style('Default', WD_STYLE_TYPE.PARAGRAPH)
    font = p.style.font
    font.name = ('Century Gothic')
    font.size = Pt(11.5)

createdocx()

document.save('Word.docx')
