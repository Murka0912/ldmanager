from untitled10.apps.monitor.models import connect

import django.conf.global_settings


print(connect.objects.values('servaddr'))