import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

url = 'https://edition.cnn.com/europe/live-news/russia-ukraine-war-news-1-16-23/index.html'

nltk.download('punkt')

article = Article(url)
article.download()
article.parse()
article.nlp()

print(f'title {article.title}')
print(f'authore {article.authors}')
print(f'publication date {article.title}')
print(f'sumery {article.title}')


