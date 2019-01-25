import xlrd
import argparse


def read_excel(file):
    wb = xlrd.open_workbook(file)
    sheet = wb.sheet_by_index(0)
    print("Number of rows: ", sheet.nrows)
    print("Number of cols: ", sheet.ncols)

    # 打印第一行信息
    print("Print First rows: ")
    for i in range(sheet.ncols):
        print(sheet.cell_value(0, i))

    # 打印第一列信息
    print("Print First columns: ")
    for i in range(sheet.nrows):
        print(sheet.cell_value(i, 0))

    print("Second Second rows: ")
    print(sheet.row_values(1))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Read excel file')
    parser.add_argument('--file', type=str, default='../data/csv/tmp.xlsx')

    config = parser.parse_args()
    read_excel(config.file)
