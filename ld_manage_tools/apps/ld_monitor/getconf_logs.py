import wmi
import pythoncom
import xml.dom.minidom as minidom
import xml.dom
import datetime
import os
import win32wnet, win32netcon

import zipfile

def connect(comp,user,pwd):
    pythoncom.CoInitialize()
    try:
        c = wmi.WMI(computer=comp, user=user, password=pwd, find_classes=False)
        return c
    except wmi.x_wmi:
        print('no connection')

srvname = 'dsud-hack-win'
user = 'lan\muravkin'
password = 'Vfrcbvrf0912!@#'
a = connect(comp=srvname, user=user, pwd=password)
que = """select * from win32_service where caption like '%landoc%' """




def connecttos(srvname1, user1, pwd1):
    try:
        win32wnet.WNetAddConnection2(win32netcon.RESOURCETYPE_DISK, None, '\\\\'+srvname1+'\\c$', None, user1, pwd1,0)
        print ('connection    established    successfully')
    except: print('connection    not established')


def config(srv, path):
    file= str('\\\\' + srv + '\\'+path+'.config')
    filelog = open(file, "r", encoding='utf-8')

    line = filelog.read().strip()
    return line

connecttos(srvname, user, password)
i=0

for s in a.query(que):
    try:
        #print(s.pathname)
        i+=1
        conffile = str(s.pathname)
        conf = conffile.replace(':', '$')
        if FileNotFoundError:
            conf = conf.replace('exe','dll')
            fff = config(srvname, conf)

        else:
            conf = conf.replace('dll','exe')
            fff = config(srvname, conf)
        with open('D:/as/'+str(s.caption)+'-'+str(s.systemname)+'.config', 'w', encoding='utf-8') as f:
            f.write(fff)
            f.close()
        continue

    except FileNotFoundError as e:
        conf = conf.replace('dll', 'exe')
        fff = config(srvname, conf)
        with open('D:/as/'+str(s.caption)+'-'+str(s.systemname)+'.config', 'w', encoding='utf-8') as f:
            f.write(fff)
            f.close()



dirs = 'D:\\as\\'

for dirs,path ,file, in os.walk(dirs):
    for g in file:
        path=dirs+g

        dom = minidom.parse(path)

        elem = dom.getElementsByTagName('appender')
        for s in elem:
            if s.attributes['name'].value == '_DailyLogFile':
                elem1 = s.getElementsByTagName('file')
                for d in elem1:
                    logfile = str(d.attributes['value'].value)
                    print(logfile)