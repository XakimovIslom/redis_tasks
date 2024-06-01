from time import sleep
from celery import shared_task
import logging
import requests
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


@shared_task()
def celery_task():
    res = requests.get("https://www.olx.uz/nedvizhimost/kvartiry/")
    soup = BeautifulSoup(res.content, "html.parser")
    list_cards = soup.find(attrs={"class": "listing-grid-container"})
    for cards in list_cards.find_all(attrs={"type": "list"}):
        print(cards.text)
    return "Done"