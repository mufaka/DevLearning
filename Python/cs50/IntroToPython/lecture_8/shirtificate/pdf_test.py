import sys
from fpdf import FPDF 

class Shirtificate(FPDF):
    def __init__(self, orientation, format):
        super().__init__(orientation=orientation, format=format)

    def header(self):
        self.set_font("helvetica", "B", 30)
        self.ln(10)        
        self.cell(0, 0, "CS50 Shirtificate", border=0, align="C")
        self.ln(20)        

def main():
    name = input("Name: ")

    if len(name) == 0:
        sys.exit("No name entered.")
    else:
        write_pdf(name)

def write_pdf(name):
    pdf = Shirtificate(orientation="Portrait", format="A4")
    pdf.add_page()
    pdf.image("shirtificate.png", x=0)
    pdf.set_font("Times", size=24)
    pdf.set_text_color(255,255,255)
    pdf.cell(0, -300, f"{name} took CS50", align="C")
    pdf.output("shirtificate.pdf")   

if __name__ == "__main__":
    main()    