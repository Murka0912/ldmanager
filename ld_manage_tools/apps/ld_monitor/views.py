import pythoncom
import wmi
import xlwt
import os
from . import conwm as mon
from . import sqlmon
from django.shortcuts import render
from django.http import HttpResponse, response
from . models import subd, usedb, disks, settings_app, applogs, methodData,urlData,synthData, result_all_tasks, Category, Medo2_2
from .models import connect_to_server as con
from .models import mon_data as monk
from django.views.generic import DetailView, ListView
from .forms import connectForm, SubdForm, setting_form ,add_url, add_method_form, urlData, CategoryForm
from django.views.decorators.clickjacking import xframe_options_exempt
from django.db.models.functions import TruncSecond,TruncMinute, TruncDate
import json
from datetime import datetime, date
from decimal import Decimal
from django.db.models import Count
from django.db import connection
import subprocess




# получение данных из бд

def connect(comp,user,pwd):
    pythoncom.CoInitialize()
    try:
        c = wmi.WMI(computer=comp, user=user, password=pwd, find_classes=False)
        return c
    except wmi.x_wmi:
        err = 'Невозможно подключится к серверу ' + str(comp)
        ss = applogs.objects.create(text=err)
        ss.save


def services(request):
    value = con.objects.all()
    for g in value:
        service = mon.services(connect(g.servaddr,g.login,g.paswd))
        return render(request, 'monitor/services.html', {'service': service,
                                                     'srv':value})

def manage_service(request):
    value=con.objects.all()
    for g in value:
        if request.method == 'POST':
            service_name = request.POST.getlist('service_name')
            checked_serv = request.POST['check']
            useservice = request.POST['choiceuse']

            if 'stop' in useservice:

                print(checked_serv, useservice)
            return render(request, 'monitor/services.html')


def current_datetime(request):

    now = datetime.datetime.now()

    html = "<html><body>It is now %s.</body></html>" % now

    return HttpResponse(html)
import random
from django.core.management import call_command


def show_result_task(request):

    a='#'
    return render(request, 'monitor/result_tasks.html', {'a':a})
def download(request):
    cat = Category.objects.all()
    return render(request, 'monitor/download.html', {'cat':cat})



from .translater import tr

def exportDataxls(request, slug, name):
    tempname = tr(str(name))
    content = 'attachment; filename="'+tempname+'.xls"'
    print(content)
    response = HttpResponse(content_type='monitor/res.html')
    response['Content-Disposition'] = content

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Disks')

    # Sheet header, first row
    row_num = 0
    borders = xlwt.Borders()
    borders.bottom = 1
    borders.left = 1
    borders.right = 1
    borders.top = 1
    borders.bottom_colour = 0
    borders.right_colour = 0
    borders.left_colour = 0
    borders.top_colour = 0
    font_style = xlwt.XFStyle()

    font_style.font.bold = True

    columns = ['Адрес сервера', 'Имя диска', 'Свободно места Gb', 'Всего места Gb', 'Дата' ]
    font_style = xlwt.XFStyle()

    font_style.borders = borders

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
        cells = xlwt.Column(col_num,ws)
        cells.set_width = 5000
       # rows = disks.objects.filter(srv__cat=slug).distinct('srvaddr').order_by('id')
    rows = disks.objects.raw("""select * from monitor_disks md where id in(select max(md1.id) id from monitor_disks md1 group by md1."namedisk", md1.srvaddr)
and md.srv_id in (select mcts.id_serv  from monitor_connect_to_server mcts where mcts.cat_id = """+slug+')')

    #rows = disks.objects.all().values_list('srvaddr', 'namedisk', 'freespace', 'allspace', 'date_up').order_by('-date_up')
    #rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime) else x for x in row] for row in rows]
    for row in rows:
        row_num += 1
        a = [row.srvaddr,row.namedisk,row.freespace,row.allspace,str(row.date_up.date())]
        print(row.date_up.date())
        for col_num in range(len(a)):
            ws.write(row_num, col_num, a[col_num], font_style)
        #
        #ws.write(row_num, , [[row.srvaddr],[row.namedisk], [str(row.freespace)],[str(row.allspace)],[row.date_up]], font_style)

    wb.save(response)
    return response



import datetime
from . import get_logs
def get_logs_func(request):
    get_logs.logs('dsud-hack-win')
    log = get_logs.get_date_files()
    print(log)
    return


import win32netcon, win32wnet


def connecttos(srvaddr, login, pswd):

    model = con.objects.all()

    try:
        win32wnet.WNetAddConnection2(win32netcon.RESOURCETYPE_DISK, None, '\\\\'+srvaddr+'\\c$', None, login, pswd,0)
        print ('connection    established    successfully')
    except: print('connection    not established')
import json
def dashboard(request):
    model = monk.objects.all()
    temp_list = []
    full_list=[]
    for g in model:

        temp_list.append(str(g.data.date()))
        full_list.append(g.cpu)

    dates = json.dumps(temp_list)
    cpu = json.dumps(full_list)
    data = {
        'model':model,
        'xdata': dates,
        'ydata':cpu,



    }
    return render(request, 'monitor/srvform.html', data)

from xml.dom import Node, minidom, DOMException
def chagexml(dir):
    xmldoc = minidom.parse(dir)
    finder = xmldoc.getElementsByTagName("xdms:organization")[0]
    DocN = xmldoc.getElementsByTagName("xdms:number")[0]
    DateDoc = xmldoc.getElementsByTagName("xdms:date")[0]
    return finder.firstChild.data, DocN.firstChild.data, DateDoc.firstChild.data
def medo(request):
    dirs = "E:\\2.2\\2.2\\"
    dest_folder = "e:\\2.2\\dest\\"

    paths = os.listdir(dirs)
    res = []
    model = Medo2_2.objects.all()
    if request.method == 'POST':
        model.delete()

        for path, folder, files in os.walk(dirs):
            if len(files) > 3:
                for file in files:
                    if file.endswith('xml'):
                        path_to_xml = path + '\\' + file
                        result, DocN, DateDoc = chagexml(path_to_xml)
                        print('Тип документ  - путь: ', path, ' Адрес: ', result, '|№ дока:', DocN, 'от', DateDoc)

                        print(path, datetime.datetime.utcfromtimestamp(os.stat(path).st_ctime).strftime('%Y-%m-%d'))
                        type_packet = 'Тип Документ'
                        p= Medo2_2.objects.create(PacketType=type_packet, Addr=result, Ndoc=DocN, DateDoc=DateDoc)
                        p.save()
                        temp = result+','+'docn: '+ DocN+'от '+ DateDoc
                        res.append(temp)
            else:
                for file in files:
                    if file.endswith('xml'):
                        path_to_xml = path + '\\' + file
                        result, DocN, DateDoc = chagexml(path_to_xml)
                        print('Тип документ  - путь: ', path, ' Адрес: ', result, '|№ дока:', DocN, 'от', DateDoc)

                        print(path, datetime.datetime.utcfromtimestamp(os.stat(path).st_ctime).strftime('%Y-%m-%d'))
                        type_packet = 'Квитанция'
                        p= Medo2_2.objects.create(PacketType=type_packet, Addr=result, Ndoc=DocN, DateDoc=DateDoc)
                        p.save()
                        temp = result+','+'docn: '+ DocN+'от '+ DateDoc
                        res.append(temp)

    return render(request, 'monitor/medo.html', {'model':model})



def index(request):
    ss = con.objects.all()
    bd = subd.objects.all()
    cat = Category.objects.all()
    url_model = urlData
    err = 'Данные не корректны'
    if request.method == "POST":
        form = connectForm(request.POST)
        form1 = SubdForm(request.POST)
        form2 = add_url(request.POST)
        form3 = add_method_form(request.POST)
        form4 = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
        if form1.is_valid():
            form1.save()
            val = subd.objects.all()
            usedb.objects.all().delete()
            for g in val:

                s = sqlmon.connecttosql(g.subdaddr,'msdb',g.username,g.password)
                got = sqlmon.dbname(s)
                print(g.subdaddr)
                for i in got:
                    print(i[0])
                    save = usedb.objects.create(subd=g.subdaddr, namedb=i[0])
                    save.save()
        if form2.is_valid():
            form2.save()
        if form3.is_valid():
            form3.save()
        if form4.is_valid():
            form4.save()
        else:
            err
    form = connectForm()
    form1 = SubdForm()
    form2 = add_url()
    form3 = add_method_form()
    form4 = CategoryForm()
    return render(request, 'monitor/main.html', {'form': form,
                                                 'form1': form1,
                                                 'form2':form2,
                                                 'form3': form3,
                                                 'form4':form4,
                                                 'error': err,
                                                 'df':ss,
                                                 'bd':bd,
                                                 'cat':cat})

def srvform(request):
    count = con.objects.count()
    mm = monk.objects.all()
    return render(request, 'monitor/srvform.html', {'mm':mm})
def listsrv(request):
    cat = Category.objects.all()
    ss = con.objects.all()
    bd = subd.objects.all()
    return render(request, 'monitor/srv.html',{'df':ss,
                                               'cat':cat,
                                                 'bd':bd})

def srv(request):
    return render(request,'monitor/srv1.html')

class SubdDetailView(DetailView):
    model = subd
    template_name = 'monitor/sql.html'
    context_object_name = 'subd'

    def get_context_data(self, **kwargs):
        """
        This has been overridden to add `car` to the template context,
        now you can use {{ car }} within the template
        """
        context = super().get_context_data(**kwargs)
        context['usedb'] = usedb.objects.all()
        return context
import json
class monitorDetail(ListView):
    try:
        model = monk
        template_name = 'monitor/preferences.html'
        context_object_name = 'pref'
        def get_queryset(self):

            return monk.objects.filter(server__id_serv=con.id_serv)

        def get_context_data(self, *, object_list=None, **kwargs):
            context = super().get_context_data(**kwargs)
            context['srvaddr'] = str(context['pref'])

            context['cpu'] = context['pref'][0]

            dates = []

            for a in monk.objects.all():

                dates.append(str(a.data.date()))

            context['date'] = json.dumps(dates)

            return context

    except FileNotFoundError:
        print('No such log file or directory')

def monDetail(request, id_srv):
    mondata = monk.objects.filter(server_id=id_srv).order_by('-id')[:40]
    disks_data = disks.objects.filter(srv_id=id_srv).filter()

    rows = disks.objects.raw("""SELECT  DISTINCT ON (md."namedisk", md.srvaddr) *  from monitor_disks md  where md.date_up = current_date order by md.srvaddr  """)
    '''"""rows = disks.objects.raw("""SELECT b.*
        FROM monitor_disks A 
        INNER JOIN monitor_disks AS B ON A.srvaddr = B.srvaddr AND A.ID < B.ID
        where b.date_up > datetime('now','-1 hour') and b.srv_id =""" + str(id_srv) + """ 
        group by b.srvaddr,b.namedisk""")"""'''
    dates = []
    cpu = []
    memory = []
    ms = []
    free = []
    dd = dict()
    nd=[]

    con_date = con.objects.filter(id_serv=id_srv)
    for mons in con_date:
        connecttos(mons.servaddr,mons.login,mons.paswd)
        #log = logs(mons.servaddr)
    for g in mondata:
        dates.append(str(g.data.date()))
        cpu.append(g.cpu)
        memory.append(g.percmem)
        ms.append(g.mem)
    for i in rows:
        allfree = []
        disks_data = disks.objects.filter(srv_id=id_srv, namedisk=i.namedisk)[:10]
        nd.append(i.namedisk)

        for s in disks_data:

            allfree.append(s.freespace)
            dd[i.namedisk] = allfree


        free.append(allfree)
    date1 = json.dumps(dates)
    cpu1 = json.dumps(cpu)
    mem = json.dumps(memory)
    mum = json.dumps(ms)
    a = con.objects.all()
    data = {'date':date1,
            'srv':a,
            'cpu':cpu1,
            'mem':mem,
            'mum':mum,
            'namesrv':g.srvaddr,
            'disks':disks_data,
            'namedisk':rows,
            'free':dd,
            #'log':log
            }
    return render(request,'monitor/preferences.html',data)

def result(request):
    #mon.connect('dusd-fkc-tst')


    return render(request, "monitor/SRV1.html")

def res(request):
    value = con
    count = con.objects.count()
    ss = disks


    dan = monk.objects.order_by('-id')[0:count]
    count1 = disks.objects.raw(
        """SELECT  DISTINCT ON (md."namedisk", md.srvaddr) *  from monitor_disks md 
         where md.date_up = current_date order by md.srvaddr  """)
    '''count1 = disks.objects.raw("""SELECT b.*
FROM monitor_disks A 
INNER JOIN monitor_disks AS B ON A.srvaddr = B.srvaddr AND A.ID < B.ID
where b.date_up > datetime('now','-1 day')
group by b.srvaddr,b.namedisk""")'''

    return render(request, 'monitor/res.html', {'mem':count1,
                                                'srvlist':value,
                                                     'dan':dan,

                                                     })
import configparser

class resultList(ListView):
    model = monk
    template_name = 'monitor/test.html'
    context_object_name = 'res1'

    def get_queryset(self):
        count = con.objects.filter(cat__slug=self.kwargs['cat_slug']).count()
        print(count)
        return monk.objects.filter(category__slug=self.kwargs['cat_slug']).order_by('-id')[0:count]
    def get_context_data(self, **kwargs):
        """
        This has been overridden to add `car` to the template context,
        now you can use {{ car }} within the template
        """
        context = super().get_context_data(**kwargs)
        context['mem'] = disks.objects.raw("""select distinct id ,  main.namedisk , main.srvaddr ,main.date_up ,main.freespace, main.allspace  from monitor_disks main right  join  
(
select  md."namedisk", md.srvaddr, max(date_up) dateUp from monitor_disks md group by md."namedisk", md.srvaddr) t
on t.namedisk=main.namedisk and t.srvaddr=main.srvaddr and t.dateUp=main.date_up
where id in 
(
select max(md1.id) id from monitor_disks md1 group by md1."namedisk", md1.srvaddr)""")

       # context['mem'] = disks.objects.raw("""SELECT b.*
    #FROM monitor_disks A
   # INNER JOIN monitor_disks AS B ON A.srvaddr = B.srvaddr AND A.ID < B.ID
   # where b.date_up > datetime('now','-1 day')
    #group by b.srvaddr,b.namedisk""")
        return context
def navbar(request):
    cat = Category.objects.all()
    return render(request, 'monitor/newbar.html', {'cat':cat})


def settings(request):
    model = settings_app.objects.all()
    mod = settings_app

    err = 'Данные не корректны'
    if request.method == "POST":
        model.delete()
        form = setting_form(request.POST)
        if form.is_valid():
            form.save()
        else:
            err
    form = setting_form()
    return render(request, 'monitor/settings.html',{'set_form':form,
                                                    'set':model})



#обновление метрик


#обновление места на дисках




from statistics import mean

def synth(request):
    model3 = urlData.objects.all()
    model1 = synthData.objects.all().order_by('-id')[:15]
    model2 = methodData.objects.all()
    dict1 = dict()
    exec_date = []

    for s in model2:
        exec_time = []
        for d in synthData.objects.filter(name_method1=s.name_method, method_fk_id=s.id). order_by('-exec_date')[:40]:

            exec_time.append(d.exec_time)

            exec_date.append(str(d.exec_date.date()))

        dict1[d.name_method1] = exec_time
    print(dict1)
    dates = json.dumps(exec_date)

    return render(request, 'monitor/synth.html', {'SynthData': model1,
                                                  'MethodData':model2,
                                                  'urlData':model3,
                                                  'dates':dates,
                                                  'xdata':dict1
                                                  })



def call_proc(request):
    sql = sqlmon.connecttosql('dsud-hack-win', 'ld','dba','sql')
    result = sqlmon.call_proc(sql,1000,'Test Annotation',5)
    print(result)
    return HttpResponse(result)

def applog(request):
    model = applogs.objects.all().order_by('-date')[:15]
    return render(request, 'monitor/logs.html', {'logs':model})

def detail(request):
    ss = con.objects.all()
    return render(request, 'monitor/preferences.html', {'ss':ss})
def listdb(request):
    dd = subd.objects.all()
    return render(request, 'monitor/sql.html', {'dblist':dd})


def dbname(request):
    val = usedb

    return render(request, 'monitor/sql.html', {'dbname': val})


def query(request):
    value = subd.objects.all()
    for g in value:
        if request.method == "POST":
            srvaddr =request.POST['srvaddr']
            print(srvaddr)
            bd = request.POST['choice_bd']

            que = request.POST['choice_query']
        s = sqlmon.connecttosql(srvaddr, bd, g.username,g.password)
        if que =='delay':
            got = sqlmon.delays(s)
            html = 'Задержки на базе '+bd
            return render(request, 'monitor/SQL/delays.html', {'delay1': got,
                                                        'text':html,
                                                       'srvaddr':srvaddr})
        elif que =='indexes':
            got = sqlmon.indexfrag(s)
            html ='Фрагментация индексов на бд '+ bd
            return render(request, 'monitor/SQL/fragindex.html', {'delay1': got,
                                                       'text': html,
                                                          'srvaddr':srvaddr})
        elif que == 'loadque':
            got = sqlmon.loadqueries(s)
            html = 'Топ запросов '
            return render(request, 'monitor/SQL/loadquery.html', {'delay1': got,
                                                          'text': html,
                                                          'srvaddr': srvaddr})
        elif que == 'status':
            got = sqlmon.status(s)
            html = 'Что происходит на сервере '
            return render(request, 'monitor/SQL/sqlstatus.html', {'delay1': got,
                                                              'text': html,
                                                              'srvaddr': srvaddr})
        elif que == 'indexcount':
            got = sqlmon.indexcount(s)
            html = 'итоговое число отсутствующих индексов для каждой базы данных '
            return render(request, 'monitor/SQL/indexcount.html', {'delay1': got,
                                                              'text': html,
                                                              'srvaddr': srvaddr})
        elif que == 'notindexload':
            got = sqlmon.non_index_load(s)
            html = 'Отсутствующие индексы, вызывающие издержки '
            return render(request, 'monitor/SQL/not_index_load.html', {'delay1': got,
                                                              'text': html,
                                                              'srvaddr': srvaddr})
        elif que == 'notusedindex':
            got = sqlmon.not_used_index(s)
            html = 'Не используемые индексы '
            return render(request, 'monitor/SQL/notusedindex.html', {'delay1': got,
                                                              'text': html,
                                                              'srvaddr': srvaddr})
        elif que == 'in_out_queries':
            got = sqlmon.in_out_queries(s)
            html = 'Запросы с высокими издержками на ввод-вывод '
            return render(request, 'monitor/SQL/in_out_queries.html', {'delay1': got,
                                                              'text': html,
                                                              'srvaddr': srvaddr})
        elif que == 'cpu_use':
            got = sqlmon.cpu_used_queries(s)
            html = 'Запросы с высоким использованием ресурсов ЦП '
            return render(request, 'monitor/SQL/cpu_use.html', {'delay1': got,
                                                              'text': html,
                                                              'srvaddr': srvaddr})
        elif que == 'blocked_queries':
            got = sqlmon.blocked_queries(s)
            html = 'Запросы, страдающие от блокировки '
            return render(request, 'monitor/SQL/blocked_queries.html', {'delay1': got,
                                                              'text': html,
                                                              'srvaddr': srvaddr})
        elif que == 'in_out_load':
            got = sqlmon.in_out_load(s)
            html = 'нагрузку на подсистему ввода-вывода '
            return render(request, 'monitor/SQL/in_out_load.html', {'delay1': got,
                                                              'text': html,
                                                              'srvaddr': srvaddr})
        elif que == 'who_cpu':
            got = sqlmon.who_cpu(s)
            html = 'нагрузку на подсистему ввода-вывода '
            return render(request, 'monitor/SQL/who_cpu.html', {'delay1': got,
                                                              'text': html,
                                                              'srvaddr': srvaddr})
        elif que == 'control':
            got = sqlmon.control(s)
            html = 'контроль "несжатости" '
            return render(request, 'monitor/SQL/control.html', {'delay1': got,
                                                              'text': html,
                                                              'srvaddr': srvaddr})
        elif que == 'operation_statistic':
            got = sqlmon.operation_statistic(s)
            html = 'статистика по операциям в БД '
            return render(request, 'monitor/SQL/opertion_stat.html', {'delay1': got,
                                                              'text': html,
                                                              'srvaddr': srvaddr})
        elif que == 'update_date_stat':
            got = sqlmon.update_date_stat(s)
            html = 'дата обновления статиститки '
            return render(request, 'monitor/SQL/update_date_stat.html', {'delay1': got,
                                                              'text': html,
                                                              'srvaddr': srvaddr})
        elif que == 'in_out_file_load':
            got = sqlmon.in_out_file_load(s)
            html = 'i/o-нагрузка на файлы '
            return render(request, 'monitor/SQL/in_out_file_load.html', {'delay1': got,
                                                              'text': html,
                                                              'srvaddr': srvaddr})
        elif que == 'in_out_disk_load':
            got = sqlmon.in_out_disk_load(s)
            html = 'i/o-нагрузка на диски '
            return render(request, 'monitor/SQL/in_out_disk_load.html', {'delay1': got,
                                                              'text': html,
                                                              'srvaddr': srvaddr})
        elif que == 'disk_usage':
            got = sqlmon.disk_usage(s)
            html = 'Занимаемое место на диске '
            return render(request, 'monitor/SQL/disk_usage.html', {'delay1': got,
                                                              'text': html,
                                                              'srvaddr': srvaddr})
        elif que == 'memory_objects':
            got = sqlmon.memory_objects(s)
            html = 'Под какие объекты выделена память '
            return render(request, 'monitor/SQL/memory_objects.html', {'delay1': got,
                                                              'text': html,
                                                              'srvaddr': srvaddr})






