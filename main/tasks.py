from .models import News
from celery import shared_task
import requests
import re




@shared_task
def create_news():

    random_title = requests.get('https://fish-text.ru/get?type=title&format=html').text
    random_content = requests.get('https://fish-text.ru/get?type=sentence&number=20&format=html').text

    new_news = News.objects.create(title=re.sub('<[^<]+?>', '', random_title),
                                   content=re.sub('<[^<]+?>', '', random_content))
    return new_news.title

