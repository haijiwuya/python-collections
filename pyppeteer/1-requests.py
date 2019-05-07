import requests
from pyquery import PyQuery as pq

url = 'http://quotes.toscrape.com/js/'
response = requests.get(url)
doc = pq(response.text)
print('Quotes:', doc('.quotes').length)

'''
    结果是0，证明使用requests是无法正常抓取到相关数据的。由于页面是JavaScript渲染而成的，我们所看到的内容是
    网页加载后又执行了JavaScript之后才呈现出来的，因此这些条目数据并不存在于原始HTML代码中，而requests仅仅抓
    取的是原始HTML代码
'''
import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('http://quotes.toscrape.com/js/')
    doc = pq(await page.content())
    print('Quotes:', doc('.quote').length)
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())

'''
    通过使用Pyppeteer，可以看到launch方法新建一个Browser对象，然后赋值给browser，然后调用newPage方法相当于浏览器中新建
    了一个选项卡，同时新建了一个Page对象。然后Page对象调用了goto方法就相当于在浏览器中输入了这个URL，浏览器跳转到了对应
    的页面进行加载，加载完成之后再调用content方法，返回当前浏览器页面的源代码。然后进一步，我们用pyquery进行解析，就可
    以得到JavaScript渲染的结果了。
'''

