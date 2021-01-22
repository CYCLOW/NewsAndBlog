import json
import requests

from .models import New

title_list = []
author_list = []
description_list = []
url_list = []

api_key = "ce469d5428b34c429269bb781eedb119"

url = "https://newsapi.org/v2/top-headlines?country=us&apiKey={}".format(api_key)

response = requests.get(url)
news_json = json.loads(response.text)

count = 5 # Number of news to read.

for news in news_json['articles']:
    if count >=0 :
        title = str(news['title'])
        author = str(news['author'])
        description = str(news['description'])
        url = str(news['url'])

        title_list.append(title)
        author_list.append(author)
        description_list.append(description)
        url_list.append(url)
        count -= 1



for i in range(0,len(title_list)):
    if New.title == title_list[i]:
        pass
    else:
        value = New(title=title_list[i], author=author_list[i], description=description_list[i], url=url_list[i])
        value.save()
        


        



