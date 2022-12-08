import wmi
import subprocess
import pythoncom

def connect(comp,user,pwd):
    pythoncom.CoInitialize()


    c = wmi.WMI(computer=comp, user=user, password=pwd, find_classes=False)

    return c
comp = connect('dsud-fkc-tst','lan\muravkin','Vfrcbvrf0912!@#')
def call_command(command):
    process=subprocess.Popen('powershell '+command, shell=True)
    stdout_value = process.communicate()[0]
    a = str(stdout_value)
    return "u'"+a
que ="SELECT * FROM Win32_LogicalDisk where drivetype=3"

for a in comp.query(que):
    print(a)
print('\n')
"""que1 = "SELECT * FROM Win32_process where name like '%lANDOCS%'"


for i in comp.query(que1):
    print(i.name, '     :    ', float(int(i.virtualsize)/1024)/1024, 'Mb')"""
def disk(comp):
    disks = comp.Win32_LogicalDisk(DriveType=3)
    return [(i.name, i.freespace, i.size) for i in disks]
f = disk(comp)

for a in f:
    print(a[0],a[1], a[2])