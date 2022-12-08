import wmi
import re, os
from subprocess import Popen, PIPE, call
import pythoncom




def get_srvmonit(comp):
    """

    :type computer: basestring
    """
    # checked WMI perf adapter service

    #uptime
    try:
        chek_que = """select * from win32_service where name = 'wmiApSrv'"""
        for chek in comp.query(chek_que):
            info = str(chek.caption) + ' ' + str(chek.state) + ' ' + str(chek.systemname)
            print(info)
            err = 'Служба была не запущена, сейчас должно быть всё ок'
            if chek.state == 'stopped':
                chek.startservice
            else:
                err
        uptimeque = "SELECT * FROM Win32_PerfFormattedData_PerfOS_System"

        for secs_up in comp.query(uptimeque):
            continue
        hours_up = int(secs_up.SystemUpTime) / 3600
    #print('uptime: '+str(hours_up)+' часов')
    #cpu
        que = "SELECT * FROM Win32_Processor"
        for a in comp.query(que):
            print('erly cpu', a.LoadPercentage)
            if a.LoadPercentage != None:
                cpu = a.LoadPercentage
            else:
                cpu = 0
            info1 = 'Запись данных сервера ' + str(a.SystemName) + ' успешна'
            print('cpu is', cpu)
    #avmem
        percque1 = 'SELECT * FROM Win32_PerfFormattedData_PerfOS_Memory'
        for almem in comp.query(percque1):
            continue
        available_mbytes = int(almem.AvailableMBytes)
    #print('доступная память: '+str(available_mbytes)+' Mb')
    #allmem
        qmem = "SELECT * FROM Win32_PerfFormattedData_PerfOS_Memory"

        for ozu in comp.query(qmem):
            continue
        allmem = float(int(ozu.CommittedBytes) / 1024) / 1024
        percque= 'SELECT * FROM Win32_PerfFormattedData_PerfOS_Memory'
        for qq in comp.query(percque):
            continue
        pct_in_use = int(qq.PercentCommittedBytesInUse)
    #print('Используется: ' + str(pct_in_use) + ' %\n')

        disks = comp.Win32_LogicalDisk(DriveType=3)


        return round(hours_up, 2),cpu,allmem, available_mbytes,pct_in_use, [(i.name, i.freespace, i.size) for i in disks], info, info1, err
    except AttributeError:
        print('no connect to PC')


def ping(host_name):
    p = Popen('ping -n 1 ' + host_name, stdout=PIPE)
    m = re.search('Average = (.*)ms', p.stdout.read())
    if m:
        return ('ok')
    else:
        raise Exception
#print(get_srvmonit('dsud-fkc-tst'))
def disk(comp):
    try:
        disks = comp.Win32_LogicalDisk(DriveType=3)
        return [(i.name, i.freespace, i.size) for i in disks]
    except AttributeError as e:
        print(e)

def services(comp):
    query = """SELECT * FROM Win32_service"""
    return ([(i.name, i.state, i.systemname) for i in comp.query(query)])

def stop_service(comp, name_service):
    for service in comp.Win32_Service(Name=name_service):
        result, = service.StopService()
        if result == 0:
            print("Service", service.Name, "stopped")

        else:
            print("Some problem")

        break
    else:
        print("Service not found")


def start_service(comp, name_service):
    for service in comp.Win32_Service(Name=name_service):
        result, = service.StartService()
        if result == 0:
            print("Service", service.Name, "stopped")

        else:
            print("Some problem")

        break
    else:
        print("Service not found")


def restart_service(comp, name_service):
    for service in comp.Win32_Service(Name=name_service):
        result, = service.RestartService()
        if result == 0:
            print("Service", service.Name, "stopped")

        else:
            print("Some problem")

        break
    else:
        print("Service not found")




