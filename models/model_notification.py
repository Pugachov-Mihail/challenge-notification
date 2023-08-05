def notification_entity(item) -> dict:
    return {
        "id": str(item['_id']),
        "day_week": item['day_week'],
        "periodicity": item['periodicity'],
        "period": item['period'],
        "time_start": item['time_start'],
        "time_end": item['time_end']
    }


def notifications_entity(entity) -> list:
    return [notification_entity(item) for item in entity.to_list(length=20)]

