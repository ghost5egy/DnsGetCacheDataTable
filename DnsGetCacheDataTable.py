import ctypes
from ctypes.wintypes import HANDLE,DWORD,LPWSTR

khandle = ctypes.WinDLL('kernel32.dll')
dhandle = ctypes.WinDLL('DNSAPI.dll')

class dnscacheentry(ctypes.Structure):
    _fields_ = [
        ("pNext", HANDLE),
        ("recName", LPWSTR),
        ("wType", DWORD),
        ("wDataLength", DWORD),
        ("dwFlags",DWORD)
    ]

dnsentry = dnscacheentry()

dnsentry.wDataLength = 1024

response = dhandle.DnsGetCacheDataTable(ctypes.byref(dnsentry))

if response == 0:
    print("failed due error {0}".format(khandle.GetLastError()))

dnsentry = ctypes.cast(dnsentry.pNext , ctypes.POINTER(dnscacheentry))

while True:
    try:
        print("Dns Entry is {0} with type {1}".format(dnsentry.contents.recName , dnsentry.contents.wType))
        dnsentry = ctypes.cast(dnsentry.contents.pNext , ctypes.POINTER(dnscacheentry))
    except:
        break
