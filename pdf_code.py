from fpdf import FPDF

class MakePDF:
    def __init__(self, article_name, article_price):
        self.pdf = FPDF(orientation="P", unit="mm", format="A4")
        self.pdf.add_page()
        self.article_name = article_name
        self.article_price = article_price

    def receipt(self, receipt_num):
        self.pdf.set_font(family="Times", size=16, style="B")
        self.pdf.cell(w=50, h=8, txt=f"Receipt nr.{receipt_num}", ln=1)

        self.pdf.set_font(family="Times", size=16, style="B")
        self.pdf.cell(w=50, h=8, txt=f"Article: {self.article_name}", ln=1)

        self.pdf.set_font(family="Times", size=16, style="B")
        self.pdf.cell(w=50, h=8, txt=f"Price: {self.article_price}", ln=1)

        self.pdf.output(f"receipt{receipt_num}.pdf")


if __name__ == "__main__":
    make_pdf = MakePDF(article_name="laptop sven", article_price="10.99")
    make_pdf.receipt(receipt_num=1)
    make_pdf1 = MakePDF(article_name="laptop sven", article_price="10.99")
    make_pdf1.receipt(receipt_num=2)
