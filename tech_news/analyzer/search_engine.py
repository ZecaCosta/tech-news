from tech_news.database import search_news


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
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
