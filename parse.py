# coding=utf8

import bs4


class Record:
    def __init__(self, person, school, money, no, category, year):
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


def parse_table(keyword, category):
    html = read_file(keyword, category, 1)

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
            r = Record(tds[0].string, tds[1].string, tds[2].string, tds[3].string, tds[4].string, tds[6].string)
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
        print "%d: (%s, %s, %s, %s, %s, %s, %s, %s)" % (cnt, r.person, r.school, r.money, r.no, r.category, r.name, r.year, r.subject)
        cnt += 1


if __name__ == "__main__":
    records = parse_table("数据", "面上项目")
    print_records(records)
