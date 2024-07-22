## update_blogPost.py
from datetime import datetime
import feedparser

blog_url = "https://kimhyun5u.tistory.com/rss"
rss_feed = feedparser.parse(blog_url)

MAX_NUM = 5

# 현재 날짜와 시간을 문자열로 변환
current_time = datetime.now().strftime("%Y-%m-%d")

latest_posts = ""

for idx, item in enumerate(rss_feed['items']):
  if idx > MAX_NUM:
     break;
  feed_date = item['published_parsed']
  latest_posts += f" - [{feed_date.tm_year}/{feed_date.tm_mon}/{feed_date.tm_mday} - {item['title']}]({item['link']})\n"

latest_posts += f"\n\nupdated at {current_time}"

preREADME = """"""
with open('base_README.md', 'r', encoding='utf-8') as file:
    preREADME = file.read()


resultREADME = f"{preREADME}{latest_posts}"

with open("README.md", "w", encoding='utf-8') as f :
  f.write(resultREADME)
