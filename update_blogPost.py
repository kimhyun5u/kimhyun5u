## update_blogPost.py
import feedparser

blog_url = "https://kimhyun5u.tistory.com/rss"
rss_feed = feedparser.parse(blog_url)

MAX_NUM = 5

latest_posts = ""

for idx, item in enumerate(rss_feed['items']):
  if idx > MAX_NUM:
     break;
  feed_date = item['published_parsed']
  latest_posts += f" - [{feed_date.tm_year}/{feed_date.tm_mon}/{feed_date.tm_mday} - {item['title']}]({item['link']})\n"


preREADME = """"""
with open('base_README.md', 'r', encoding='utf-8') as file:
    preREADME = file.read()


resultREADME = f"{preREADME}{latest_posts}"

with open("README.md", "w", encoding='utf-8') as f :
  f.write(resultREADME)
