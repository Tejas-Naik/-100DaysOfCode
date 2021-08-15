from bs4 import BeautifulSoup
# If you want to use lxml
# import lxml   --> inside the parser "lxml"

with open("website.html", encoding="utf-8") as file:
    contents = file.read()

#soup = HTML file
soup = BeautifulSoup(contents, 'html.parser')
# print(soup)  # .prettify())  .title  .title.name  .title.string

# if you run soup.p you will get the first p tag but if you
# want all p tags then use find_all() function


all_anchor_tags = soup.find_all('a')
# if you wanna print all href's then
for tag in all_anchor_tags:
    print(tag.getText())        # If you wanna get the text
    print(tag.get('href'))      # THis is equal to tag.href

# if you want to get the heading only when there are more than one h1 tags
heading = soup.find(name="h1", class_='myname')
# heading = soup.find(name='h1', id='name!')
print(heading.getText())

# if you want to search as a CSS selector like (p a) which is 'a' inside 'p' tag
a_in_p = soup.select_one(selector='p a')
print(a_in_p.get('href'))