from bs4 import BeautifulSoup
from lxml import html
import requests

# Request the page
# page = requests.get('https://webscraper.io/test-sites/e-commerce/allinone')
# tree = html.fromstring(page.content) 
# print(page.content)
# prices = tree.xpath(
#     '//div[@class="col-sm-4 col-lg-4 col-md-4"]/div/div[1]/h4[1]/text()')
# print(prices)
# re = requests.get("http://econpy.pythonanywhere.com/ex/001.html")

page = requests.get('https://www.bmw.com/en/automotive-life/bmw-3-series-generations.html')
tree = html.fromstring(page.content)
# generations = tree.xpath(
#     '/html/body/main/article/div[1]/div/div[6]/div/div/div/div[1]/div[1]/h2/text()'
# )
generations = tree.find_elements_by_xpath(
    '//div[@class="pw-m-listicle__headline"]')
for span in generations:
    print (span.text)
# built = tree.xpath(
#     '/html/body/main/article/div[1]/div/div[6]/div/div/div/div[1]/div[3]/ul/li[1]/strong/text()'
# )
# power = tree.xpath(
#     '/html/body/main/article/div[1]/div/div[6]/div/div/div/div[1]/div[3]/ul/li[2]/strong/text()'
# )
# variants = tree.xpath(
#     '/html/body/main/article/div[1]/div/div[6]/div/div/div/div[1]/div[3]/ul/li[3]/strong/text()'
# )
# print(generations)
# print(built)
# print(power)
# print(str(variants) + '\n')

# generations2 = tree.xpath(
#     '/html/body/main/article/div[1]/div/div[13]/div/div/div/div[1]/div[1]/h2/text()'
# )

# generations3 = tree.xpath(
#     '/html/body/main/article/div[1]/div/div[20]/div/div/div/div[1]/div[1]/h2/text()'
# )

# print(generations2)
# print(generations3)
