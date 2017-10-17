# -*- coding:utf-8 -*-
import wmi,sys
if len(sys.argv)<4:
  print("Please check the command parameters! For example:[pwmi.py ip username password]")

script,cip,cuser,cpass = sys.argv
w=wmi.WMI(computer=cip, user=cuser, password=cpass)
# w=wmi.WMI(computer="191.168.3.27", user="woody", password="woody2lsuwindows")
# w=wmi.WMI(computer="191.168.2.111", user="wangwei", password="wangwei")
# w=wmi.WMI(computer="191.168.6.77", user="administrator", password="MERIT1998")

# for processor in w.Win32_Processor():
#   print("Processor ID: %s" % processor.DeviceID)
#   print("Process Name: %s" % processor.Name.strip())
# totalMemSize=0
# for memModule in w.Win32_PhysicalMemory():
#   totalMemSize+=int(memModule.Capacity)
# print ("Memory Capacity: %.2fMB" %(totalMemSize/1048576))
#
for process in w.Win32_Process ():
  print("%5s  %s" % (process.ProcessId, process.Name) )

# for pm in w.Win32_PhysicalMedia():
#   print("%s" % ( pm.tag) )

# for battary in w.Win32_Battery():
#     for key in battary.__dict__:
#         print(key, ':', battary.__dict__[key])
#   # print("%s" % (battary.Chemistry) )


