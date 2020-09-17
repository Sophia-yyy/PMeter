"""
封装get、post方法，判断接口是否能请求
"""
import requests
from Pubilc.DoExcel import ReadExcel
from Config import globalconfig
import os
import json
# from Pubilc.DoExcel import WriteExcel


class DoRequest():

    def __init__(self, excel_name, sheet_name):
        self.excel_name=excel_name
        self.sheet_name=sheet_name
        self.ini_ip = globalconfig.project_ip  # 从配置文件读取项目的IP
        self.ini_host = globalconfig.project_host  # 从配置文件读取项目的host
        self.rows = ReadExcel( self.excel_name, self.sheet_name).get_rows()  # 读取测试用例EXCEL的总行数

# 根据读取的EXCEL的方法，判断执行get还是post方法，返回状态码和response
    def doRequest(self):
        i = 1
        result_list =[]
        while i < self.rows:
            excel_url = ReadExcel(self.excel_name, self.sheet_name).read_excel(i, 1)  # 读取测试用例EXCEL的路径
            excel_method = ReadExcel(self.excel_name, self.sheet_name).read_excel(i, 2)  # 读取测试用例EXCEL的方法
            excel_parm = json.loads(
                ReadExcel(self.excel_name, self.sheet_name).read_excel(i, 3))  # 读取测试用例EXCEL的传参
            url = 'http://' + self.ini_ip + ':' + self.ini_host + excel_url  # 拼接测试接口的URL

            if excel_method == 'get':
                 result=DoRequest(self.excel_name, self.sheet_name).getMethod(url, excel_parm)
                 result_list.append(result)

            elif excel_method == 'post':
                pass

            i = i + 1
        return result_list
        # print(result_list)

    def getMethod(self, url, excel_parm):
        try:

            r = requests.get(url, params=excel_parm, timeout=30)
            r.raise_for_status()  # 如果状态不是200，引发HTTPError异常
            r.encoding = r.apparent_encoding
            # print(r.status_code)
            return r.status_code,r.text # 返回状态码和返回值

        except Exception as e :
            return e

            # print('错误类型是', e.__class__.__name__)
            # print('错误明细是', e)


# 调试DoRequest类，可注释
if __name__ == '__main__':
    demo = DoRequest('bike1.xlsx', 'Sheet1').doRequest()
    print(demo)


    # print(demo.getMethod())
    # WriteExcel(Excelname,Sheetname).write_excel(1,5,demo.get_method())
