from apscheduler.schedulers.background import BackgroundScheduler
from .utils import update_model


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_model, 'interval', hours=23, minutes=59)
    scheduler.start()
