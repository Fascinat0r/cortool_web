from celery import Celery

from app.config import REDIS_HOST, REDIS_PORT

celery = Celery('tasks', broker=f'redis://{REDIS_HOST}:{REDIS_PORT}')
