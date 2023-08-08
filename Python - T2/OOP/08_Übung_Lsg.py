class Article:

    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price
        
class ShoppingCart:

    def __init__(self):
        self.articles = []
        
    def show_articles(self):
        for article in self.articles:
            print(article.name)
        
    def add_article(self, article: Article):
        self.articles.append(article)
        
    def remove_article(self, article_name: str):
        for article in self.articles.copy():
            if article.name == article_name:
                self.articles.remove(article)      
        
    def get_sum(self):
        sum_price = 0
        for article in self.articles:
            sum_price += article.price
        
        return sum_price
        
article_list = [
    Article("Monitor", 200),
    Article("Tastatur", 80),
    Article("Kabel", 10)
]

for elem in article_list:
    print(f"Name: {elem.name}")
    print(f"Preis: {elem.price}")
    print()
    

my_shopping_cart = ShoppingCart()
my_shopping_cart.add_article(article_list[0])
my_shopping_cart.add_article(article_list[0])
my_shopping_cart.add_article(article_list[2])

print("Dein Warenkorb enthält:")
my_shopping_cart.show_articles()
print(f"Gesamtpreis =", my_shopping_cart.get_sum())


my_shopping_cart.remove_article("Monitor")
print("Dein Warenkorb enthält:")
my_shopping_cart.show_articles()
print(f"Gesamtpreis =", my_shopping_cart.get_sum())

