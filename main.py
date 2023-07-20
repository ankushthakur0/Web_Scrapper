from bs4 import BeautifulSoup
from pprint import pprint
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

# req = requests.get('https://www.bmw.com/en/automotive-life/bmw-3-series-generations.html')
 
# print(req.encoding)    
# print(req.status_code)
# print(req.elapsed)    
# print(req.url)        
# print(req.history)    
# print(req.headers['Content-Type'])

# page = requests.get('https://www.bmw.com/en/automotive-life/bmw-3-series-generations.html')
# tree = html.fromstring(page.content)
# generations = tree.xpath(
#     '/html/body/main/article/div[1]/div/div[13]/div/text()'
# )
# print(generations)




# URL = "https://www.bmw.com/en/automotive-life/bmw-3-series-generations.html"
# URL = "http://www.values.com/inspirational-quotes"
# r = requests.get(URL)
  
# soup = BeautifulSoup(r.content, 'html5lib') 
# # print(soup.prettify())

# generations = []
# table = soup.find('div', attrs = {'id':'all_quotes'}) 
# print(table)


resp = requests.get('https://www.bmw.com/en/automotive-life/bmw-3-series-generations.html')

# parse the page
page = BeautifulSoup(resp.content)

# relevant class attributes found by just looking at the site html 
# in a browser, you may need to alter it slightly to get the desired divs 

# find_all works very similarly to querySelectorAll
# for x in page.find_all(attrs={'class': 'col col--s4 has-nested-row'}):
#     # get text will pull all inner text from child elements of selected 'x' elem
#     # print(x.get_text())
#     for y in x.find_all(attrs={'class': 'pw-m-listicle__headline'}):
        
#         for a in y.find_all(attrs={'class': 'hl hl--m'}):
#             print(a.get_text())

# for generation in page.find_all(attrs = {'class': 'hl hl--m'}):
#     print(generation.get_text())

for build in page.find_all(attrs = {'class': 'strong'}):
    print(build.get_text())

for power in page.find_all(attrs = {'class': 'li'}):
    print(power.get_text())

for variants in page.find_all(attrs = {'class': 'li'}):
    print(variants.get_text())




def main():
    url = 'https://www.bmw.com/en/automotive-life/bmw-3-series-generations.html'
    for elem in BeautifulSoup(requests.Session().get(url).text, 'lxml').find_all('div', {'class': 'pw-m-listicle'})[::2]:
        pprint({
            'Generation': elem.find('div', {'class': 'pw-m-listicle__headline'}).text,
            **{list_elem.text.split(':')[0].strip() : list_elem.text.split(':')[-1].strip() for list_elem in elem.find_all('li')},
            'Description': "\n".join([p.text for p in elem.find('p')])
        })

if __name__ == '__main__':
    main()



# r = requests.get("https://www.bmw.com/en/automotive-life/bmw-3-series-generations.html")
 
# data = r.text
# soup = BeautifulSoup(data)
 
# for link in soup.find_all('a'):
    # print(link.get('href'))


# from lxml import etree
 
# root_elem = etree.Element('html')
# etree.SubElement(root_elem, 'head')
# etree.SubElement(root_elem, 'title')
# etree.SubElement(root_elem, 'body')
 
# print(etree.tostring(root_elem, pretty_print = True).decode("utf-8"))





# generations = tree.find_elements_by_xpath(
#     '//div[@class="pw-m-listicle__headline"]')
# for span in generations:
#     print (span.text)
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
