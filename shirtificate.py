from fpdf import FPDF, Align

pdf = FPDF(orientation="P", format="A4")
question = f"{input('Name: ')} took CS50"
pdf.add_page()
pdf.set_font("helvetica", "", 45)   #""обычный шрифт не курсив и не жирный
pdf.set_text_color(0, 0, 0)
pdf.text(50, 40, "CS50 Shirtificate")   #это расположение в середине
pdf.image("shirtificate.png", x=0, y=60)
pdf.set_font("helvetica", "", 25)
pdf.set_text_color(255, 255, 255)   #это белый цвет
pdf.cell(0, 240, question, align=Align.C)

pdf.output("shirtificate.pdf")
