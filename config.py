import os
import gevent.monkey
gevent.monkey.patch_all()

import multiprocessing

pidfile = "log/gunicorn.pid"
accesslog = "log/access.log"
errorlog = "log/debug.log"
daemon = True

# 启动的进程数
workers = multiprocessing.cpu_count()
worker_class = 'gevent'
x_forwarded_for_header = 'X-FORWARDED-FOR'

SECREY_KEY = os.urandom(50)