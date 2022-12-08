

from celery import shared_task
from .models import result_all_tasks, connect_to_server as con, mon_data as monk, applogs, disks, methodData,urlData, synthData
from .  import conwm as mon
import wmi
import pythoncom
from .request1 import auth,request_resp
from django.utils import timezone
import datetime

def connect(comp,user,pwd):
    pythoncom.CoInitialize()
    try:
        c = wmi.WMI(computer=comp, user=user, password=pwd, find_classes=False)
        return c
    except wmi.x_wmi:
        err = 'Невозможно подключится к серверу ' + str(comp)
        ss = applogs.objects.create(text=err)
        ss.save
#обновление метрик
@shared_task()
def update_stat(cat):

    try:
        value = con.objects.filter(cat_id=cat)
        for g in value:
            a, b, ozu, c, d, diskmem,info,info1,err = mon.get_srvmonit(connect(g.servaddr, g.login, g.paswd))
            if monk.objects.count() > 1000000000:
                monk.objects.first().delete()
            else:
                p = monk.objects.create(srvaddr=g.servaddr, uptime=a,server_id=g.id_serv,category=g.cat, cpu=b,allmem=ozu, mem=c, percmem=d, disks=diskmem)
                p.save()

                applog = applogs.objects.create(text=info)
                applog.save()
                applog = applogs.objects.create(text=info1)
                applog.save()
                applog = applogs.objects.create(text=err)
                applog.save()
    except TypeError:
        print('Type error 1')



#обновление места на дисках
@shared_task()
def disk_update(cat):
    d = datetime.datetime.now()
    try:
        value = con.objects.filter(cat_id=cat)
        for g in value:

            diskmem = mon.disk(connect(g.servaddr,g.login,g.paswd))
            for space in diskmem:
                save = disks.objects.create(srvaddr=g.servaddr,date_up=d, namedisk=space[0],srv_id=g.id_serv, freespace=round(float(space[1])/1073741824, 3),
                                        allspace=round(float(space[2])/1073741824, 3))
                save.save()
        return print('запись данных о дисках завершена')
    except TypeError:
        err = 'Error проверьте подключение к серверу, либо службу WMI Perfomance Adapter'
        ss = applogs.objects.create(text=err)
        ss.save()
@shared_task()
def syntec():
    model1 = methodData.objects.all()
    synadd = synthData.objects.all()

    model2 = urlData.objects.all()
    for g in model2:
        for c in model1:
            req_url = g.url + c.method
            aut, headers = auth(g.login, g.passwd, g.url)
            resp = request_resp(aut.cookies, req_url, headers)
            print(resp.elapsed.total_seconds(), resp.url, resp.status_code)
            save = synadd.create(name_method1=c.name_method,method_fk_id=c.id, exec_time=resp.elapsed.total_seconds())
            save.save()
    return print('запись ок!')
"""celery -A untitled10 worker -E --loglevel=INFO --without-gossip --without-mingle --without-heartbeat -Ofair --pool=solo
celery -A untitled10 beat -l info --scheduler=django_celery_beat.schedulers:DatabaseScheduler"""

