#coding:utf8
import psutil

pythons_psutil = []
for p in psutil.process_iter():
    try:
        if p.name() == 'python.exe':
            pythons_psutil.append(p)
    except psutil.Error:
        pass
for i in pythons_psutil:
    print(i)
