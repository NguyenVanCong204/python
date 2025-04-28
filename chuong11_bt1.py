from lxml import html
import requests
page = requests.get('https://www.youtube.com/watch?v=DWYwmTdXpqw&list=RD3s1r_g_jXNs&index=3&ab_channel=AnhT%C3%BAOfficial')
tree = html.fromstring(page.content)

print(page)
print(tree)

print(page.text)
# print(html.tostring(tree, pretty_print=True).decode())