from __future__ import absolute_import

import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orange.settings')
app = Celery('orange')
app.config_from_object('django.conf:settings')


@app.task()
def submit_sms_mt_request_task(payload, message):
    from orangeapisms.utils import do_submit_sms_mt_request
    return do_submit_sms_mt_request(payload, message)
