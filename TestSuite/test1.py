# 尝试把DoRequest和validate连起来
# 判断状态码是否符合预期

from Pubilc.DoRequests import DoRequest
from Pubilc.validate import equals
from Pubilc.DoExcel import ReadExcel


# 解析拿到的状态码
def get_code(excelname, sheetname):
    result = DoRequest(excelname, sheetname).doRequest()
    code_list = []
    for i in range(len(result)):
        status = result[i]
        status_code = status[0]
        code_list.append(status_code)
        # print(status_code)
    return code_list


# 判断EXCEL中的状态码预期结果是否和实际相同
def judgStatusCode(excelname, sheetname):
    status_code = get_code(excelname, sheetname)
    # except_code = ReadExcel(excelname, sheetname).read_excel(1, 4)
    result_list = []
    for i in range(len(status_code)):
        result = equals(status_code[i], ReadExcel(excelname, sheetname).read_excel(i + 1, 4))
        result_list.append(result)
    return result_list


if __name__ == "__main__":
    test1 = get_code('bike1.xlsx', 'Sheet1')
    test2 = judgStatusCode('bike1.xlsx', 'Sheet1')
    print(test1)
    print(test2)
