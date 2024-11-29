# requests模块的使用
import requests

if __name__ == "__main__":
    # 指定url
    url = 'https://www.bing.com/search?q=123&form=ANNTH1&refig=6749989a4d374414b7da94e62db28ff9&pc=U531'
    # 发起请求
    # get方法会返回一个响应对象

    # 持久化存储
    with open('.test/sogou.html', 'w', encoding='utf-8') as fp:
        fp.write(requests.get(url= url).text)
    print('爬取数据结束！')

