"""
读取配置文件获取配置文件信息
读取测试用例、测试报告、日志文件路径
"""
import os
from Pubilc.ReadConfigIni import ReadConfigIni

# 读取配置文件
# 获取config.ini的路径

file_path = os.path.split(os.path.realpath(__file__))[0]
# print(file_path)

# 读取配置文件
read_config = ReadConfigIni(os.path.join(file_path, "config.ini"))
# print(read_config)

# 借助config.ini获取项目的参数
# 获取项目路径
project_path = read_config.getConfigValue('project', 'project_path')
# print(project_path)

# 获取项目IP
project_ip = read_config.getConfigValue('ip', 'ip')
# print(project_ip)

# 获取项目端口
project_host = read_config.getConfigValue('host', 'host')
# print(project_host)

# 日志路径
log_path = os.path.join(project_path, 'Report', 'Log')
# print(log_path)

# 测试用例路径
TestCase_path = os.path.join(project_path, 'TestCase')
# print(TestCase_path)

# 测试报告路径
report_path = os.path.join(project_path, 'Report', 'TestReport')
# print(report_path)
