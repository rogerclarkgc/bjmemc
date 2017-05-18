from __future__ import absolute_import
from datetime import timedelta
from celery.schedules import crontab

CELERY_TIMEZONE = 'Asia/Shanghai'

# IMPORTANT!! IMPORT THE TASK MODULE
CELERY_IMPORTS = ('test_celery')
# IMPORTANT!! SET THE BROKER AND BACKEND SERVER
BROKER_URL = 'redis://localhost'
CELERY_RESULT_BACKEND = 'redis://localhost'

# THE SCHEDULE OF MY TASK
# BEAWARE!! 'task' key is MY specified task's FILENAME
# NOTE: use '.' to represent the child module or function of MY task module
CELERYBEAT_SCHEDULE = {
    'add-every-1min':{
        'task':'test_celery.run',
        'schedule': crontab(minute = '*/1'),
        'args':()
    }
}