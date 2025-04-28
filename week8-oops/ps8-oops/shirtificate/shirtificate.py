from fpdf import FPDF

# pdf = FPDF(orientation="P",unit="mm",format="A4")
# pdf.add_page()
# pdf.set_margins(0,0,0)
# pdf.set_font('Arial','B',14)
# pdf.cell(w=40,h=10,txt='Hello World!',border=0,ln=1,align='',fill=False,link='')

# # Add New Line In the pdf
# pdf.set_font('Times','',12)
# pdf.cell(210,10,'Powered by FPDF',0,0,'C')
# pdf.image('shirtificate.png',x=85,y=32.5,w=40,h=0,type='',link='')
# pdf.output("sample.pdf","F")

class PDF(FPDF):
    def header(self):
        # Rendering logo:
        self.image("shirtificate.png", 10, 8, 33)
        # Setting font: helvetica bold 15
        self.set_font("helvetica", style="B", size=15)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 10, "Title", border=1, align="C")
        # Performing a line break:
        self.ln(20)

    def footer(self):
        # Position cursor at 1.5 cm from bottom:
        self.set_y(-15)
        # Setting font: helvetica italic 8
        self.set_font("helvetica", style="I", size=8)
        # Printing page number:
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")


# Instantiation of inherited class
pdf = PDF()
pdf.add_page()
pdf.set_font("Times", size=12)
for i in range(1, 41):
    pdf.cell(0, 10, f"Printing line number {i}", ln=1)
pdf.output("new-tuto2.pdf")