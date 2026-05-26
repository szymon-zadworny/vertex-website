import os
import sys
import datetime
import mistune
from collections import OrderedDict


class Article:
    date: datetime
    title: str
    content_path: str

    def __init__(self, date, title, content_path):
        self.date = date
        self.title = title
        self.content_path = content_path
    

    def convert_to_html(self):
        file = open(self.content_path)
        html = mistune.html(file.read())
        return html


def get_articles(path):
    articles = OrderedDict()
    dirs = [os.path.join(path, f) for f in os.listdir(path)]

    for dir in dirs:
        if not os.path.isdir(dir):
            continue
        posts = [os.path.join(dir, f) for f in os.listdir(dir)]

        for post in posts:
            if not os.path.isdir(post):
                continue
            key = ""
            date = os.path.basename(dir)
            key += date
            date = date.split('-')
            date = datetime.datetime(int(date[0]), int(date[1]), int(date[2]))
            title = os.path.basename(post)
            key = os.path.join(key, title)
            title = title.split('-')[1:]
            title = " ".join(title)
            content_path = os.path.join(post, os.path.basename(post))
            content_path = "".join([content_path, ".md"])
            article = Article(date, title, content_path)
            articles[key] = article
            print(key)
    
    return articles