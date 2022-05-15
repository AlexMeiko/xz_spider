import requests 
import os
from lxml import etree
from fake_useragent import UserAgent
from multiprocessing.dummy import Pool as ThreadPool

Threads = 26 #线程数
Start_Page = 1 #起始页
End_Page = 1 #结束页

def request_header():
    headers = {
        'User-Agent': UserAgent().Chrome
    }
    return headers

def send_request():
    for i in range(Start_Page,End_Page+1):
        print(f'正在抓取第{i}页……')
        response = requests.get(url=f'https://diskgirl.com/imageslist?page={i}', headers=request_header())
        text = response.text.encode('UTF-8')
        html = etree.HTML(text)
        div_list = html.xpath('/html/body//div[@class="cover-title"]')
        thread_down(div_list,i)
    print('抓取完成！')

def get_pic(title,url,page):
    proxies = {
        #"http": "http://" + proxy,
        #"https": "http://" + proxy
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

def thread_down(div_list,page):
    pool = ThreadPool(Threads)
    for a in div_list:
        url = 'https://diskgirl.com' + a.xpath('./a/@href')[0].replace('image', 'images')
        title = a.xpath('./a/h2/text()')[0]
        pool.apply_async(get_pic, (title,url,page))
    pool.close()
    pool.join()

if __name__ == '__main__':
    send_request()
