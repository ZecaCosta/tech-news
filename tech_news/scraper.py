# reference: https://docs.python.org/3/library/time.html
import time

# reference: https://docs.python-requests.org/en/master/
import requests


# Requisito 1
def fetch(url):
    try:
        r = requests.get(url, timeout=3)
        time.sleep(1)
        if r.status_code == 200:
            return r.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
