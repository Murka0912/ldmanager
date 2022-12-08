
import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ld_manage_tools.settings')
s = os.environ.setdefault('CELERY_CONFIG_MODULE', 'celeryconfig')
app = Celery('untitled10')
#app.config_from_object('django.conf:settings', namespace='CELERY')

#app.config_from_object(Config)
app.config_from_envvar('CELERY_CONFIG_MODULE')
app.autodiscover_tasks()
#https://docs.microsoft.com/ru-ru/windows/wsl/install-manual

if __name__ =='__main__':
    app.start(['beat','--loglevel=INFO','--scheduler=django_celery_beat.schedulers:DatabaseScheduler'])
"""if __name__ =='__main__':
    app.start(['beat','--loglevel=INFO','--scheduler=django_celery_beat.schedulers:DatabaseScheduler'])"""

"""celery -A untitled10 worker -E --loglevel=INFO --without-gossip --without-mingle --without-heartbeat -Ofair --pool=solo
celery -A untitled10 beat -l info --scheduler=django_celery_beat.schedulers:DatabaseScheduler
(['worker','-E','--loglevel=INFO','--without-gossip','--without-mingle','--without-heartbeat',
               '-Ofair','--pool=solo'])
(['beat','--loglevel=INFO','--scheduler=django_celery_beat.schedulers:DatabaseScheduler'])"""
    