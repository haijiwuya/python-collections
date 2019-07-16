import requests
import json
import os

def spider_comment():
    """
    抓取某东评论数据
    :return:
    """
    url = "https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv4654&productId=1263013576&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1"
    '有时抓取数据需要加上请求头参数才可以'
    kv = {"user-agent": "Mozilla/5.0", "Referer": 'https://item.jd.com/1263013576.html'}
    try:
        r = requests.get(url, headers=kv)
        r.raise_for_status()
        '通过对爬取的数据分析，此数据为jsonp跨域请求返回的json结果，所以我们只要把前面的fetchJSON_comment98vv4646(和最后的)去掉就拿到json数据了'
    except:
        print("抓取失败")
    # 获取json数据字符串
    r_json_str = r.text[26: -2]
    r_json_obj = json.loads(r_json_str)
    # 获取评价列表数据
    r_json_comments = r_json_obj['comments']
    print("某东评论数据:")
    # 写入数据之前先清空之前的数据
    comment_file_path = "D://a.txt"
    if os.path.exists(comment_file_path):
        os.remove(comment_file_path)
    # 遍历评价列表数据
    for r_json_comment in r_json_comments:
        # 获取评论对象中的评论内容
        print(r_json_comment['content'])
        with open(comment_file_path, 'a+') as file:
            file.write(r_json_comment['content'] + '\n')


if __name__ == '__main__':
    spider_comment()
