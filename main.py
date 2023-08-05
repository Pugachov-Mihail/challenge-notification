import requests
from celery import Celery

from config.settings import REDIS_DB_URL

app = Celery(__name__, broker=REDIS_DB_URL)


def request_api(url: str):
    request = requests.get(url).json()
    return [item for item in request]


def _create_data_in_mongodb():
     res = request_api("localhost:8080/get_notification")
     confi_db.db.values.insert_many([_data_for_mongo(i) for i in res])
     list_data = confi_db.db.values.find({})
     return notifications_entity(list_data)


def _data_for_mongo(item: Notification):
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