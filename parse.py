# coding=utf8

import bs4
import os


import sys
reload(sys)
sys.setdefaultencoding('utf8')


class Record:
    def __init__(self, keyword, person, school, money, no, category, year):
        self.keyword = keyword
        self.person = person
        self.school = school
        self.money = money
        self.no = no
        self.category = category
        self.year = year
        self.name = ""
        self.subject = ""


def read_file(keyword, category, page):
    file_object = open('html/%s-%s-%s.html' % (keyword.decode("utf-8"), category.decode("utf-8"), page), 'r')
    html = file_object.read()
    file_object.close()
    return html


def parse_table_for_all_pages(keyword, category):
    records = []
    page = 1
    while os.path.exists("html/%s-%s-%s.html" % (keyword.decode("utf-8"), category.decode("utf-8"), page)):
        tmp = parse_table(keyword, category, page)
        records.extend(tmp)
        page += 1
    return records


def parse_table(keyword, category, page):
    html = read_file(keyword, category, page)

    soup = bs4.BeautifulSoup(html, "html.parser")
    # print soup.prettify()

    trs = soup.find(class_="table_yjfx").find_all(name='tr')
    cnt = 0
    records = []
    for tr in trs:
        tds = tr.find_all(name="td")
        if len(tds) == 0 or len(tds) == 1:
            continue

        print str(cnt) + ": ",
        if cnt % 3 == 0:
            r = Record(keyword, tds[0].string, tds[1].string, tds[2].string, tds[3].string, tds[4].string, tds[6].string)
            if r.category is None:
                if float(r.money) < 100:
                    r.category = "面上项目"
                else:
                    r.category = "重点项目"

            records.append(r)
        elif cnt % 3 == 1:
            records[-1].name = tds[1].string
        else:
            records[-1].subject = tds[1].string

        for td in tds:
            print td.string,
        print ""

        cnt += 1

    print ""
    return records


def print_records(records):
    cnt = 0
    for r in records:
        print "%d: (%s, %s, %s, %s, %s, %s, %s, %s, %s)" % (cnt, "11", r.person, r.school, r.money, r.no, r.category, r.name, r.year, r.subject)
        cnt += 1


def get_records():
    records = []
    records.extend(parse_table_for_all_pages("安全", ""))

    # records.extend(parse_table_for_all_pages("安全", "面上项目"))
    print_records(records)
    return records


# 面上项目
# 重点项目
# 青年科学基金项目
# 优秀青年基金项目
# 海外或港、澳青年学者合作研究基金
# 国际(地区)合作与交流项目
if __name__ == "__main__":
    get_records()
