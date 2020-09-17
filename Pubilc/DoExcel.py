"""
分装读EXCEL方法
EXCEL中放置接口路径、方法、传参
"""
import xlrd
import xlwt
import os
from Config import globalconfig

TestCase_path = globalconfig.TestCase_path


class ReadExcel():
    # 读取其他目录下的Excel文件
    def __init__(self, filename, sheetname):
        testcase_path = os.path.join(TestCase_path, filename)
        self.workbook = xlrd.open_workbook(testcase_path)
        self.sheetname = self.workbook.sheet_by_name(sheetname)

    # 获取EXCEl有多少行
    def get_rows(self):
        rows = self.sheetname.nrows
        return rows

    # 读取某个单元格的数据
    def read_excel(self, crownum, colnum):
        value = self.sheetname.cell(crownum, colnum).value
        return value


class WriteExcel():
    # 创建Excel文件
    def __init__(self, filename, sheetname):
        # testcase_path = os.path.join(TestCase_path, filename)
        self.filename = filename
        # self.workbook = xlwt.Workbook(testcase_path)
        self.workbook = xlwt.Workbook(encoding='utf-8')
        self.sheetname = self.workbook.add_sheet(sheetname)
    def table(self):
        # 我也不知道在这里定义表头好不好，暂时这样吧

        self.sheetname.write(0, 0, label='接口名称')
        self.sheetname.write(0, 1, label='路径')
        self.sheetname.write(0, 2, label='方法')
        self.sheetname.write(0, 3, label='传参')
        self.sheetname.write(0, 4, label='预期')
        self.sheetname.write(0, 5, label='结果')
        self.sheetname.write(0, 6, label='是否通过')
        # self.workbook.save(self.filename)  # 保存

    def write_excel(self, crownum, colnum, label):
        self.sheetname.write(crownum, colnum, label=label)  # 写入excel,参数对应 行, 列, 值

        # self.workbook.save(self.filename)

    def save_excel(self):
        self.workbook.save(self.filename)  # 保存


# 验证ReadExcel类的正确性
if __name__ == "__main__":
    case = WriteExcel('bike2.xls', 'Sheet1').write_excel(1, 6, 200)

    print(case)
