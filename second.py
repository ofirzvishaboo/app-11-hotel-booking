import pandas
from pdf_code import MakePDF

df = pandas.read_csv("articles.csv", dtype={"name": str, "price": str, "in stock": int})

class Article:
    def __init__(self, articles_id):
        self.articles_id = articles_id
        self.name = df.loc[df["id"] == self.articles_id, "name"].squeeze()
        self.price = df.loc[df["id"] == self.articles_id, "price"].squeeze()
        self.stock = df.loc[df["id"] == self.articles_id, "in stock"].item()

    def available(self):
        print(self.stock)
        if self.stock >= 0:
            return True
        else:
            return False

    def book(self):
        df.loc[df["id"] == self.articles_id, "in stock"] = df.loc[df["id"] == self.articles_id, "in stock"] - 1
        df.to_csv("articles.csv", index=False)

    def export(self):
        make_pdf = MakePDF(article_name=f"{self.name}", article_price=f"{self.price}")
        return make_pdf


y = 1
while True:
    article_id = input("Enter id of the article: ")
    article = Article(int(article_id))
    if article.available():
        article.book()
        make_pdf = article.export()
        make_pdf.receipt(receipt_num=y)
        y = y + 1
    else:
        continue

