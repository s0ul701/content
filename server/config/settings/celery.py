import os

CELERY_BROKER_URL = (
    'amqp://'
    f'{os.environ.get("RABBITMQ_DEFAULT_USER")}:'
    f'{os.environ.get("RABBITMQ_DEFAULT_PASS")}@'
    'rabbitmq:5672/'
    f'{os.environ.get("RABBITMQ_DEFAULT_VHOST")}'
)
CELERY_IGNORE_RESULT = True
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
