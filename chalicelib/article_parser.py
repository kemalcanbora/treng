from newspaper import Article
from chalicelib.model import ArticleModel
import time

def parser(URL):
    try:
        article = Article(URL)
        while article.download_state == 0:
            time.sleep(1)
            article.download()
            try:
                article.parse()
                text = article.text
                if len(article.title) == 0:
                    title = "undefined"
                else:
                    title = article.title

                data = ArticleModel(source=article.url,
                                    text=text,
                                    name=title,
                                    crawling_time=time.time().__int__())
                return data
            except:
                data = ArticleModel(source=article.url,
                                    text=None,
                                    name=None,
                                    crawling_time=time.time().__int__())
                return data

    except EOFError as e:
        return e