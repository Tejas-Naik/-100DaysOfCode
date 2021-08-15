import requests

blog_url = "https://api.npoint.io/456e2b2881d8810340f0"
response = requests.get(blog_url)
all_blog = response.json()
print(all_blog)
