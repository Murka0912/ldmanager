import django.db.models as models
from django.utils import timezone
from django.urls import reverse
import datetime
import uuid
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255,default=uuid.uuid1, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']

class Medo2_2(models.Model):
    PacketType = models.CharField(max_length=30, verbose_name='Тип пакета')
    Addr = models.CharField(max_length=200, verbose_name='Адрес отправителя')
    Ndoc = models.CharField(max_length=50,verbose_name='№ документа')
    DateDoc = models.CharField(max_length=50, verbose_name='Рег. дата')

class connect_to_server(models.Model):
    id_serv = models.AutoField('idserv', primary_key=True)
    servaddr = models.CharField('Адрес сервера',db_index=True, max_length=100)
    login = models.CharField('логин',max_length=50)
    paswd = models.CharField('пароль', max_length=50)
    slug = models.SlugField(max_length=255,default=uuid.uuid1, unique=True, db_index=True, verbose_name="URL")
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.servaddr

    def get_absolute_url(self):

        return reverse('monk', kwargs={'con_slug': self.slug})

    class Meta:
        verbose_name = 'Адрес сервера'
        verbose_name_plural = 'Адрес сервера'
        ordering = ['id_serv']




class mon_data(models.Model):
    srvaddr = models.CharField('Адрес сервера',max_length = 100 )
    server = models.ForeignKey(connect_to_server,on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    uptime = models.FloatField('Время работы')
    cpu = models.IntegerField('cpu', null=True)
    allmem = models.FloatField('OZU')
    mem = models.IntegerField('mem')
    percmem = models.IntegerField('% используемой оперативное памяти',default=0)
    disks = models.CharField('диски', max_length=200)
    data = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=255,default=uuid.uuid1, unique=True, db_index=True, verbose_name="URL")
    def __str__(self):
        return self.srvaddr
    def get_absolute_url(self):
        return reverse('post', kwargs={'mon_slug': self.slug})

    class Meta:
        verbose_name = 'Показатели метрик'
        verbose_name_plural = 'Показатели метрик'
        ordering = ['-data', 'srvaddr']








class subd(models.Model):
    subdaddr = models.CharField('Адрес сервера СУБД', max_length=100)
    username = models.CharField('UserName', max_length=50)
    password = models.CharField('Password',max_length=50 )
    class Meta:
        verbose_name = 'Сервер СУБД'
        verbose_name_plural = 'Сервер СУБД'
        ordering = ['-id', 'subdaddr']

class usedb(models.Model):
    subd = models.CharField('СУБД',max_length=100)
    namedb = models.CharField('Имя БД', max_length=50)
    class Meta:
        verbose_name = 'Список бд в субд'
        verbose_name_plural = 'список бд в субд'
        ordering = ['-id']

class disks(models.Model):
    srvaddr = models.CharField('Адрес сервера', max_length=100)
    namedisk = models.CharField('Имя диска', max_length=10)
    srv = models.ForeignKey(connect_to_server, on_delete=models.CASCADE)
    freespace = models.FloatField('Свободное место')
    allspace = models.FloatField("Всего места")
    date_up = models.DateTimeField()
    class Meta:
        verbose_name = 'данные по дискам'
        verbose_name_plural = 'данные по дискам'
        ordering = ['-date_up', 'srvaddr']
    def was_publish(self):
        return self.date_up >= (timezone.now() - datetime.timedelta(seconds=5))


class settings_app(models.Model):
    date_update = models.DateTimeField('Время обновления настроек', default=timezone.now)
    update_period = models.IntegerField('Период обновления данных', null=True)
    class Meta:
        verbose_name = 'OPTIONS'
        verbose_name_plural = 'OPTIONS'
        ordering = ['-id']

class applogs(models.Model):
    date = models.DateTimeField('дата/время', default=timezone.now)
    text = models.CharField('text', max_length=250)
    class Meta:
        verbose_name = 'LOGS'
        verbose_name_plural = 'LOGS'
        ordering = ['-date']


class urlData(models.Model):
    url = models.CharField('url', max_length=150)
    login = models.CharField('Login', max_length=50, default='')
    passwd = models.CharField('Pass', max_length=50, default='')
    class Meta:
        verbose_name = 'адреса веб клиента'
        verbose_name_plural = 'адреса веб клиента'
        ordering = ['-id', 'url']

class methodData(models.Model):
    name_method = models.CharField('Name_method', max_length=150)
    method = models.CharField('method', max_length=200)
    class Meta:
        verbose_name = 'данные по методам WebApi'
        verbose_name_plural = 'данные по методам WebApi'
        ordering = ['-id', 'name_method']

class synthData(models.Model):
    name_method1 = models.CharField('Name_method', max_length=150, default='')
    exec_date = models.DateTimeField('Дата выполнения', default=timezone.now)
    exec_time = models.FloatField('Время выполнения')
    method_fk = models.ForeignKey(methodData, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Результат выполнения\\время выполнения'
        verbose_name_plural = 'данные по дискам'
        ordering = ['-exec_date', 'name_method1']

class result_all_tasks(models.Model):
    date_execs = models.DateTimeField('время выполнения',default=timezone.now)
    result_exec = models.IntegerField('результат')