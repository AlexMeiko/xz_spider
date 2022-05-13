import requests 
import os
from lxml import etree
from fake_useragent import UserAgent
def request_header():
    headers = {
        'User-Agent': UserAgent().Chrome
    }
    return headers

def send_request():
    open("all_post.txt", 'w').close()
    for i in range(1,2): #爬取页数(开始页,结束页+1)
        print(f'正在抓取第{i}页……')
        response = requests.get(url=f'https://diskgirl.com/imageslist?page={i}', headers=request_header())
        text = response.text.encode('UTF-8')
        html = etree.HTML(text)
        div_list = html.xpath('/html/body//div[@class="cover-title"]')
        for a in div_list:
            uri = a.xpath('./a/@href')[0]
            title = a.xpath('./a/h2/text()')[0]
            uri = uri.replace('image', 'images')
            get_pic(title,'https://diskgirl.com'+uri,i)
    print('抓取完成！')

def get_pic(title,url,page):
    print('Download:' + title)
    proxies = {
        #"http": "http://" + proxy,
        #"https": "http://" + proxy,
        # "http": proxy,
        # "https": proxy,
    }
    os.makedirs('./data/' + str(page) + '/'+ title + '/', exist_ok=True)
    for i in range(1,999):
        print('Downloading:' + url + '/' + str(i) + '.jpg')
        response = requests.get(url=url + '/' + str(i) + '.jpg' ,headers=request_header(),proxies=proxies) 
        with open('./data/' + str(page)  + '/' + title + '/' + str(i) + '.jpg', 'wb') as f:
            f.write(response.content)
        response.close()
        if response.status_code == 404:
            break

if __name__ == '__main__':
    send_request()
