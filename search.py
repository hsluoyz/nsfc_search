# coding=utf8

import requests
import re

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# https://github.com/bioinfo1992/nsfc


def save_file(keyword, category, page, html):
    file_object = open('html/%s-%s-%s.html' % (keyword.decode("utf-8"), category.decode("utf-8"), page), 'w')
    file_object.write(html)
    file_object.close()
    print "Saved to: html/%s-%s-%s.html" % (keyword, category, page)


def parse_page_number(html):
    # f = open("example.html", "r")
    # html = f.read()
    # f.close()

    s = re.search(u'共(\d*)页', html)
    return int(s.group(1).encode("utf-8"))


def search(keyword, category, page):
    print "Searching: (%s, %s), page = %d" % (keyword, category, page)

    url = "http://www.letpub.com.cn/?page=grant&name=%s&person=&no=&company=&addcomment_s1=553&addcomment_s2=563&addcomment_s3=0&money1=&money2=&startTime=2014&endTime=2017&subcategory=%s&currentpage=%d&searchsubmit=true" % (keyword, category, page)
    res = requests.get(url)
    if res.status_code != 200:
        print "Status code error: " + str(res.status_code)
    html = res.text

    page_count = -1
    if page == 1:
        page_count = parse_page_number(html)
        print "page count = %d" % page_count

    if page_count != 0:
        save_file(keyword, category, page, html)

    return page_count


def search_all_pages(keyword, category):
    page_count = search(keyword, category, 1)
    for i in range(2, page_count + 1):
        search(keyword, category, i)


# search_all_pages("数据", "面上项目")
# search_all_pages("数据", "重点项目")
# search_all_pages("数据", "重大项目")

# search_all_pages("数据", "青年科学基金项目")
# search_all_pages("数据", "优秀青年基金项目")
# search_all_pages("数据", "国家杰出青年科学基金")

# search_all_pages("数据", "海外或港、澳青年学者合作研究基金")
# search_all_pages("数据", "国际(地区)合作与交流项目")
