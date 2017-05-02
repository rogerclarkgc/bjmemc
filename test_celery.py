from __future__ import absolute_import
from celery import Celery
from celery.schedules import crontab
from celery import beat

from Crawlerbjmemc import bjmemc
# BE AWARE!! THE FIRST PARAMETER OF THE Celery() CONSTRUCTOR IS THE FILE NAME OF YOUR TASK MODULE
app = Celery('test_celery')

"""
BE AWARE!! THE 'celeryconfig.py' IS THE DEFAULT CONFIG FILE OF THE YOUR CELERY WORKER,
MUST BE IMPORTED BEFORE IT WORKS

"""
app.config_from_object('celeryconfig', force = True)

@app.task
def run():
    t = bjmemc()
    errorlist = t.runOnetask()
    print len(errorlist)