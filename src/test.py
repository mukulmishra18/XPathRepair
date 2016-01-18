from scrapy.http.response.html import HtmlResponse
from __init__ import XPathRepair

def test_basic_repair():
    f = open('test.html')
    test_response = HtmlResponse("http://www.example.com", body = f.read())
    xr = XPathRepair(test_response)
    print xr.process('item', '/html/body/div[1]/p/text()')
    print xr.process('item', '/html/body1/div[1]/p/text()')

def test_basic():
    f = open('test.html')
    test_response = HtmlResponse('http://www.example.com', body = f.read())
    print test_response.xpath('/html/body/div[1]/p/text()').extract()
    print test_response.xpath('/html/body1/div[1]/p/text()').extract()


test_basic()
test_basic_repair()
