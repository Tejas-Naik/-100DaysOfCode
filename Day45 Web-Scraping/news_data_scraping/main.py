from bs4 import BeautifulSoup
import requests
# To get the HTML
response = requests.get('https://news.ycombinator.com/news')

yc_webpage = response.text

# there are two types of parsers HTML Parser, XML Parser.
soup = BeautifulSoup(yc_webpage, 'html.parser')

# news_first = soup.select_one('.storylink')    ## the class for the news
# link = news_first.get('href')
# print(news_first.getText())
# print(link)

article_texts = []
article_links = []

articles = soup.find_all(name='a', class_='storylink')
for article in articles:
    article_texts.append(article.getText())
    article_links.append(article.get('href'))

article_upvotes = [int(score.get_text().split()[0]) for score in soup.find_all(name='span', class_='score')]   # .split()[0] = getting number only

# max voted news
maximum_up_votes = max(article_upvotes)
max_index = article_upvotes.index(maximum_up_votes)
for i in range(len(article_links) - 1):
    print(article_texts[i])
    print(article_links[i])
    print(f"Upvotes: {article_upvotes[i]}")
    print()

# all_posts = soup.find_all(name="a", class_="storylink")
# for post in all_posts:
#     print(post.getText())
#     print(post.get('href'))
#     print()