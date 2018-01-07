# coding=utf8

from openpyxl import Workbook

import parse


def write_records(records):
    wb = Workbook()
    sheet = wb.get_active_sheet()

    sheet.append(["负责人", "单位名称", "项目金额", "项目批准号", "项目类别", "批准时间", "项目名称", "学科分类"])
    for r in records:
        sheet.append([r.person, r.school, r.money, r.no, r.category, r.year, r.name, r.subject])

    wb.save(r'output/survey2.xlsx')


if __name__ == "__main__":
    records = parse.get_records()
    write_records(records)
