import requests
from celery import Celery

from config import confi_db
from config.settings import REDIS_DB_URL
from models.model_notification import notifications_entity
from shemas.notification import Notification

app = Celery(__name__, broker=REDIS_DB_URL)


def request_api(url: str):
    try:
        request = requests.get(url).json()
        return request
    except requests.exceptions.ConnectionError:
        raise requests.exceptions.ConnectionError("Ошибка подключения")


def create_data_in_mongodb():
    res = request_api("http://127.0.0.1:8000/api-notification/get_notification")
    confi_db.db.values.insert_many(res)


def _data_for_mongo(item: Notification):
    print(item)
    return {
        "day_week": item.day_week,
        "periodicity": item.periodicity,
        "period": item.period,
        "time_start": str(item.time_start),
        "time_end": str(item.time_end),
        "challenge": {
            "id": str(item.challenge.id),
            "user_id": str(item.challenge.user_id)
        }
    }


create_data_in_mongodb()
