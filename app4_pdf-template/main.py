from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics (1).csv")

for index, row in df.iterrows():
    pdf.add_page()
    # adds a new page

    pdf.set_font(family="Times", style="B", size=24)
    
    pdf.set_text_color(0, 0, 254)

    # The w and h are width and height specified for the border
    # When we have "width = 0" then it takes up the whole row 
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1, border=0)
    # To define size for new text or to change it from already existing size a whole new pdf.set_font can be created
    # ln is used to give the number of break lines hence have to be greater than 0 always
    for i in range(28):
        pdf.line(10, 21 + i*10, 200, 21 + i*10)
    
    pdf.ln(265)
    
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="R", ln=1, border=0)

    for i in range(row["Pages"]-1):
        pdf.add_page()
        pdf.ln(277)
    
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="R", ln=1, border=0)

# If the value of border is 0 then w and h have NO USE and there is no border but it is recommended to use border
# Height should be equal to the size value

pdf.output("output.pdf")