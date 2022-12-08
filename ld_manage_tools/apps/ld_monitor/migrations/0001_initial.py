# Generated by Django 3.2.8 on 2022-10-24 22:25

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='applogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='дата/время')),
                ('text', models.CharField(max_length=250, verbose_name='text')),
            ],
            options={
                'verbose_name': 'LOGS',
                'verbose_name_plural': 'LOGS',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='connect_to_server',
            fields=[
                ('id_serv', models.AutoField(primary_key=True, serialize=False, verbose_name='idserv')),
                ('servaddr', models.CharField(db_index=True, max_length=100, verbose_name='Адрес сервера')),
                ('login', models.CharField(max_length=50, verbose_name='логин')),
                ('paswd', models.CharField(max_length=50, verbose_name='пароль')),
                ('slug', models.SlugField(default=uuid.uuid1, max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Адрес сервера',
                'verbose_name_plural': 'Адрес сервера',
                'ordering': ['id_serv'],
            },
        ),
        migrations.CreateModel(
            name='Medo2_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PacketType', models.CharField(max_length=30, verbose_name='Тип пакета')),
                ('Addr', models.CharField(max_length=200, verbose_name='Адрес отправителя')),
                ('Ndoc', models.CharField(max_length=50, verbose_name='№ документа')),
                ('DateDoc', models.CharField(max_length=50, verbose_name='Рег. дата')),
            ],
        ),
        migrations.CreateModel(
            name='methodData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_method', models.CharField(max_length=150, verbose_name='Name_method')),
                ('method', models.CharField(max_length=200, verbose_name='method')),
            ],
            options={
                'verbose_name': 'данные по методам WebApi',
                'verbose_name_plural': 'данные по методам WebApi',
                'ordering': ['-id', 'name_method'],
            },
        ),
        migrations.CreateModel(
            name='result_all_tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_execs', models.DateTimeField(default=django.utils.timezone.now, verbose_name='время выполнения')),
                ('result_exec', models.IntegerField(verbose_name='результат')),
            ],
        ),
        migrations.CreateModel(
            name='settings_app',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_update', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Время обновления настроек')),
                ('update_period', models.IntegerField(null=True, verbose_name='Период обновления данных')),
            ],
            options={
                'verbose_name': 'OPTIONS',
                'verbose_name_plural': 'OPTIONS',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Srv_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Категория')),
                ('slug', models.SlugField(default=uuid.uuid1, max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='subd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subdaddr', models.CharField(max_length=100, verbose_name='Адрес сервера СУБД')),
                ('username', models.CharField(max_length=50, verbose_name='UserName')),
                ('password', models.CharField(max_length=50, verbose_name='Password')),
            ],
            options={
                'verbose_name': 'Сервер СУБД',
                'verbose_name_plural': 'Сервер СУБД',
                'ordering': ['-id', 'subdaddr'],
            },
        ),
        migrations.CreateModel(
            name='urlData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=150, verbose_name='url')),
                ('login', models.CharField(default='', max_length=50, verbose_name='Login')),
                ('passwd', models.CharField(default='', max_length=50, verbose_name='Pass')),
            ],
            options={
                'verbose_name': 'адреса веб клиента',
                'verbose_name_plural': 'адреса веб клиента',
                'ordering': ['-id', 'url'],
            },
        ),
        migrations.CreateModel(
            name='usedb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subd', models.CharField(max_length=100, verbose_name='СУБД')),
                ('namedb', models.CharField(max_length=50, verbose_name='Имя БД')),
            ],
            options={
                'verbose_name': 'Список бд в субд',
                'verbose_name_plural': 'список бд в субд',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='synthData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_method1', models.CharField(default='', max_length=150, verbose_name='Name_method')),
                ('exec_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата выполнения')),
                ('exec_time', models.FloatField(verbose_name='Время выполнения')),
                ('method_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ld_monitor1.methoddata')),
            ],
            options={
                'verbose_name': 'Результат выполнения\\время выполнения',
                'verbose_name_plural': 'данные по дискам',
                'ordering': ['-exec_date', 'name_method1'],
            },
        ),
        migrations.CreateModel(
            name='mon_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('srvaddr', models.CharField(max_length=100, verbose_name='Адрес сервера')),
                ('uptime', models.FloatField(verbose_name='Время работы')),
                ('cpu', models.IntegerField(null=True, verbose_name='cpu')),
                ('allmem', models.FloatField(verbose_name='OZU')),
                ('mem', models.IntegerField(verbose_name='mem')),
                ('percmem', models.IntegerField(default=0, verbose_name='% используемой оперативное памяти')),
                ('disks', models.CharField(max_length=200, verbose_name='диски')),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
                ('slug', models.SlugField(default=uuid.uuid1, max_length=255, unique=True, verbose_name='URL')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ld_monitor1.srv_category')),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ld_monitor1.connect_to_server')),
            ],
            options={
                'verbose_name': 'Показатели метрик',
                'verbose_name_plural': 'Показатели метрик',
                'ordering': ['-data', 'srvaddr'],
            },
        ),
        migrations.CreateModel(
            name='disks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('srvaddr', models.CharField(max_length=100, verbose_name='Адрес сервера')),
                ('namedisk', models.CharField(max_length=10, verbose_name='Имя диска')),
                ('freespace', models.FloatField(verbose_name='Свободное место')),
                ('allspace', models.FloatField(verbose_name='Всего места')),
                ('date_up', models.DateTimeField()),
                ('srv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ld_monitor1.connect_to_server')),
            ],
            options={
                'verbose_name': 'данные по дискам',
                'verbose_name_plural': 'данные по дискам',
                'ordering': ['-date_up', 'srvaddr'],
            },
        ),
        migrations.AddField(
            model_name='connect_to_server',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ld_monitor1.srv_category'),
        ),
    ]