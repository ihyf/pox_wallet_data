import requests
from lxml import etree

selector = etree.HTML("")
r = requests.get("https://www.feixiaohao.com/currencies/florincoin/")
selector = etree.HTML(r.text)
# content = selector.xpath('//div[@id="content"]/ul[@id="ul"]/li/text()')
content = selector.xpath("//span[@class='convert']")
flo_rmb = selector.xpath("//span[@class='convert']")[0].text
flo_usd = selector.xpath("//span[@class='convert']")[1].text
flo_btc = selector.xpath("//span[@class='convert']")[2].text
print(flo_rmb, flo_usd, flo_btc)
print(content)


