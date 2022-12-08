import os
import xml.dom.minidom as minidom


"""
dir = 'D:\\as\\'

for dirs,path ,file, in os.walk(dir):
    for g in file:
        path=dirs+g

        dom = minidom.parse(path)

        elem = dom.getElementsByTagName('appender')
        for s in elem:
            if s.attributes['name'].value == '_DailyLogFile':
                elem1 = s.getElementsByTagName('file')
                for d in elem1:
                    logfile = str(d.attributes['value'].value)
                    print(logfile)"""


dir = '\\\\dsud-hack-win\\c$\\programdata\\lanit\\'




def logs(srvaddr):
    try:
        dir = '\\\\' + srvaddr + '\\c$\\ProgramData\\Lanit\\LanDocs\\ContentServer\\'
        for dirs, path, files in os.walk(dir):
            for file in files:
                filedir = dir + file
                filelog = open(filedir, "r", encoding='ISO-8859-1')

                line = filelog.read().strip()
                with open('.\\logs\\'+file, 'w', encoding='ISO-8859-1') as f:
                    f.write(line)
            return line
    except FileNotFoundError:\
        print('Это не КС')


#print(logs('dsud-hack-win'))

def get_date_files():
    stroka = ''
    for dirs,path,files in os.walk('.\\logs\\'):
        for file in files:
            paths = dirs+file


            file = file.replace('LanDocsServer.','')
            file = file.replace('.log','')
            with open (paths, 'r', encoding='ISO-8859-1') as read_log:
                for f in read_log:
                    stroka += f
        return stroka

print(get_date_files())