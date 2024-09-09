from newspaper import Article
from IPython.display import display, Markdown

urls = [
    "http://cnn.com/2023/03/29/entertainment/the-mandalorian-episode-5-recap/index.html", 
    "https://www.cnn.com/2023/06/09/entertainment/jurassic-park-anniversary/index.html"
]

for url in urls:
    article = Article(url)
    article.download()
    article.parse()
    print(article.title)  # Console display for title
    print(article.text[:500])  # Display the first 500 characters
