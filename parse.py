# coding=utf8

import bs4
import re

def parse_table():
    soup = bs4.BeautifulSoup(open("example.html"), "html.parser")
    # print soup.prettify()

    trs = soup.find(class_="table_yjfx").find_all(name='tr')
    for tr in trs:
        tds = tr.find_all(name="td")
        for td in tds:
            print td.string,
        print ""


if __name__ == "__main__":
    parse_page_number()
