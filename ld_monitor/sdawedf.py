from .models import connect_to_server as connect

import django.conf.global_settings


print(connect.objects.values('servaddr'))