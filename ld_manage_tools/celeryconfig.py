REDIS_HOST = '127.0.0.1'
REDIS_PORT = '6379'
BROKER_URL = 'redis://'+REDIS_HOST+':'+REDIS_PORT+'/0'
CELERY_BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}
CELERY_RESULT_BACKEND = 'redis://'+REDIS_HOST+':'+REDIS_PORT+'/1'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ENABLE_UTC = False
CELERY_TIMEZONE = 'Europe/Moscow'