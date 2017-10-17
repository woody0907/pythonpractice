import wmi_client_wrapper as wmi

wmic = wmi.WmiClientWrapper(
    username="administrator",
    password="szsyl123",
    host="191.168.3.158"
)

output = wmic.query("SELECT * FROM Win32_Processor")
print(output)
