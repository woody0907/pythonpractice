# -*- coding: utf-8 -*-
import wmi_client_wrapper as wmi
import sys
import json

# wmic = wmi.WmiClientWrapper(
#     username="administrator",
#     password="szsyl123",
#     host="191.168.3.158"
# )

script, cip, cuser, cpass = sys.argv

wmic = wmi.WmiClientWrapper(
    username=cuser,
    password=cpass,
    host=cip
)

# 通过wmi获取不同的指标，获取方法类似
Win32_Processor = wmic.query("SELECT * FROM Win32_Processor")
Win32_Battery = wmic.query("SELECT * FROM Win32_Battery")
Win32_PortableBattery = wmic.query("SELECT * FROM Win32_PortableBattery")


outjson = {}
# 放数到输出对象中
outjson["Win32_Processor"] = Win32_Processor
outjson["Win32_Battery"] = Win32_Battery
outjson["Win32_PortableBattery"] = Win32_PortableBattery
# 将结果转换成Json并输出
pj = json.dumps(outjson)
print(pj)
