import asyncio
from pyppeteer import launch
'''
    模拟网页截图，保存PDF，还可以执行自定义的JavaScript获得特定的内容
'''

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('http://quotes.toscrape.com/js/')
    await page.screenshot(path='example.png')
    await page.pdf(path='example.pdf')
    dimensions = await page.evaluate('''() => {
            return {
                width: document.documentElement.clientWidth,
                height: document.documentElement.clientHeight,
                deviceScaleFactor: window.devicePixelRatio,
            }
        }''')

    print(dimensions)
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())