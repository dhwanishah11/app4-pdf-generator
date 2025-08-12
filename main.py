from fpdf import FPDF
import pandas as pd

df = pd.read_csv("topics.csv")

pdf = FPDF(orientation="p", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

for index, row in df.iterrows():

    #code for header
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1, border=0)
    pdf.line(10, 21, 200, 21)

    ln = 10
    y = 31
    for i in range(1,27):
        pdf.ln(10)
        pdf.line(10, y, 200, y)
        ln = ln + 10
        y = y + 10
    #set footer for parent page
    pdf.ln(2)
    pdf.set_font(family="Times", style="I", size=12)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="R", ln=1, border=0)


    for i in range(row["Pages"] - 1):
        #set footer to child pages
        pdf.add_page()
        ln = 10
        y = 21
        for i in range(1, 28):
            pdf.ln(10)
            pdf.line(10, y, 200, y)
            ln = ln + 10
            y = y + 10
        pdf.ln(2)
        pdf.set_font(family="Times", style="I", size=12)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="R", ln=1, border=0)


pdf.output("output.pdf")

