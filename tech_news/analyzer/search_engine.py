from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    query = {"title": {"$regex": f"{title}", "$options": "-i"}}
    news = search_news(query)
    if news:
        return [(new["title"], new["url"]) for new in news]
    else:
        return []


# Requisito 7
def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    query = {"timestamp": {"$regex": f"{date}"}}
    news = search_news(query)
    if news:
        return [(new["title"], new["url"]) for new in news]
    else:
        return []


# Requisito 8
def search_by_source(source):
    query = {"sources": {"$regex": f"{source}", "$options": "-i"}}
    news = search_news(query)
    if news:
        return [(new["title"], new["url"]) for new in news]
    else:
        return []


# Requisito 9
def search_by_category(category):
    query = {"categories": {"$regex": f"{category}", "$options": "-i"}}
    news = search_news(query)
    if news:
        return [(new["title"], new["url"]) for new in news]
    else:
        return []
