import requests
import json
import os
import jieba
import time
import random
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# 评论数据保存文件
COMMENT_FILE_PATH = "jd_comment.txt"
# 词云形状图片
WC_MASK_IMG = 'wawa.jpg'
# 词云字体
WC_FONT_PATH = '/Library/Fonts/Songti.ttc'

def spider_comment(page = 0):
    """
    抓取某东评论数据
    :param page: 抓取第几页，默认值为0
    :return:
    """

    url = "https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv4654" \
          "&productId=1263013576&score=0&sortType=5&page=%s&pageSize=10&isShadowSku=0&fold=1" % page
    '有时抓取数据需要加上请求头参数才可以'
    kv = {"user-agent": "Mozilla/5.0", "Referer": 'https://item.jd.com/1263013576.html'}
    try:
        r = requests.get(url, headers=kv)
        r.raise_for_status()
        '通过对爬取的数据分析，此数据为jsonp跨域请求返回的json结果，所以我们只要把前面的fetchJSON_comment98vv4646(和最后的)去掉就拿到json数据了'
    except:
        print("抓取失败")
    # 截取json数据字符串
    r_json_str = r.text[26: -2]
    # 字符串转json对象
    r_json_obj = json.loads(r_json_str)
    # 获取评价列表数据
    r_json_comments = r_json_obj['comments']
    # 遍历评价列表数据
    for r_json_comment in r_json_comments:
        # 获取评论对象中的评论内容
        print(r_json_comment['content'])
        with open(COMMENT_FILE_PATH, 'a+') as file:
            file.write(r_json_comment['content'] + '\n')

def batch_spider_comment():
    """
    批量爬取某东评价
    :return:
    """
    # 写入数据之前先清空数据
    if os.path.exists(COMMENT_FILE_PATH):
        os.remove(COMMENT_FILE_PATH)
    for i in range(100):
        spider_comment(i)
        # 模拟用户浏览，设置一个爬虫间隔，防止IP被封
        time.sleep(random.random() * 5)

def cut_word():
    """
    对数据分词
    :return: 分词后的数据
    """
    with open(COMMENT_FILE_PATH) as file:
        comment_txt = file.read()
        wordlist = jieba.cut(comment_txt, cut_all=True)
        wl = " ".join(wordlist)
        print("读取文件")
        print(wl)
        return wl

def create_word_cloud():
    """
    生成词云
    :return:
    """
    # 设置词云形状图片
    wc_mask = np.array(Image.open(WC_MASK_IMG))
    # 设置词云的一些配置，如：字体，背景色，词云形状，大小
    wc = WordCloud(background_color='white', max_words=2000, mask=wc_mask, scale=4,
                   max_font_size=50, random_state=42, font_path=WC_FONT_PATH)
    # 生成词云
    print("准备生成词云")
    wc.generate(cut_word())

    # 在只设置mask的情况下，你将会得到一个拥有图片形状的词云
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.figure()
    plt.show()

if __name__ == '__main__':
    # 爬取数据
    # batch_spider_comment()

    # 生成词云
    create_word_cloud()
