from celery import Celery

app = Celery(__name__)
app.conf.broker_url = "redis://localhost:6379"
app.conf.result_backend = "redis://localhost:6379"

@app.task
def a():
    return "eqsdaasd"

#
# async def create_data_in_mongodb(db: AsyncSession = Depends(get_db)):
#     notif = NotificationUser(db)
#     res = await notif.get_notification_current_day_week()
#     await confi_db.db.values.insert_many([_data_for_mongo(i) for i in res])
#     list_data = confi_db.db.values.find({})
#     return await notifications_entity(list_data)
#
#
# def _data_for_mongo(item: Notification):
#     return {
#         "day_week": item.day_week,
#         "periodicity": item.periodicity,
#         "period": item.period,
#         "time_start": str(item.time_start),
#         "time_end": str(item.time_end),
#         "challenge": {
#             "id": str(item.challenge.id),
#             "user_id": str(item.challenge.user_id)
#         }
#     }