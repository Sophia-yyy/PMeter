import xlwt
#未用

# 创建Excel文件


def table(sheetname):
    workbook = xlwt.Workbook(encoding='utf-8')
    sheetname = workbook.add_sheet(sheetname)

    sheetname.write(0, 0, label='接口名称')
    sheetname.write(0, 1, label='路径')
    sheetname.write(0, 2, label='方法')
    sheetname.write(0, 3, label='传参')
    sheetname.write(0, 4, label='预期')
    sheetname.write(0, 5, label='结果')
    sheetname.write(0, 6, label='是否通过')
    # self.workbook.save(self.filename)  # 保存


def write_excel(sheetname, crownum, colnum, label):
    sheetname = table(sheetname)
    sheetname.write(crownum, colnum, label=label)  # 写入excel,参数对应 行, 列, 值

    # self.workbook.save(self.filename)


def save_excel(filename,sheetname):
    workbook = table(sheetname)
    workbook.save(filename)  # 保存
