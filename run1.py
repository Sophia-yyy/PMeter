# 未用
from HTMLTestRunner import HTMLTestRunner
import time
from Config import globalconfig
import unittest
from Pubilc.DoRequests import DoRequest
from TestSuite.test1 import judgStatusCode
from Pubilc.DoExcel import WriteExcel, ReadExcel
from TestSuite.test1 import get_code
from Pubilc.WriteExcel import *

"""
执行测试用例，并生成测试报告
"""

# 测试报告所在路径
report_path = globalconfig.report_path
# 测试用例路径
TestCase_path = globalconfig.TestCase_path


def AutoRun(excelName, sheetname):
    now = time.strftime("%Y-%m-%d %H_%M_%S")  # 获取系统当前时间
    report_name = report_path + "\\" + now + "report.xls"  # 拼接测试报告名称
    test_result = judgStatusCode(excelName, sheetname)
    # print((get_code('bike1.xlsx', 'Sheet1')[0]))
    i = 0
    rows = 1
    # rows=ReadExcel(excelName,sheetname).get_rows()
    # WriteExcel(report_name, 'Sheet1').table()
    table(sheetname)
    while i < len(test_result):
        # # 写入excel有点问题
        write_excel('Sheet1',rows,0,ReadExcel(excelName, sheetname).read_excel(rows, 0))
        write_excel('Sheet1', rows, 1, ReadExcel(excelName,sheetname).read_excel(rows,1))
        # WriteExcel(report_name, 'Sheet1').write_excel(rows, 0,
        #                                               ReadExcel(excelName, sheetname).read_excel(rows, 0))  # 写入接口名称
        # WriteExcel(report_name, 'Sheet1').write_excel(rows, 1, ReadExcel(excelName,sheetname).read_excel(rows,1))  # 路径
        # # WriteExcel(report_name, 'Sheet1').write_excel(rows, 2, ReadExcel(excelName,sheetname).read_excel(rows,2))  # 写入是否通过
        # # WriteExcel(report_name, 'Sheet1').write_excel(rows, 3, ReadExcel(excelName,sheetname).read_excel(rows,3))  # 写入是否通过
        # # WriteExcel(report_name, 'Sheet1').write_excel(rows, 4, ReadExcel(excelName,sheetname).read_excel(rows,4))  # 写入是否通过
        # # WriteExcel(report_name, 'Sheet1').write_excel(rows, 5,  (get_code('bike1.xlsx', 'Sheet1')[i]))  # 写入是否通过
        # # WriteExcel(report_name, 'Sheet1').write_excel(rows, 6, test_result[i]) # 写入是否通过
        # print(ReadExcel(excelName, sheetname).read_excel(rows, 0))
        i = i + 1
        rows = rows + 1

    save_excel(report_name,sheetname)

    # WriteExcel(report_name, 'Sheet1').save_excel()


if __name__ == "__main__":
    AutoRun('bike1.xlsx', 'Sheet1')
