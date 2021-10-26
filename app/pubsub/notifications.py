from time import time
import json

from flask import make_response, jsonify

from db_access import db_action
from firebase_config import sendPush

notifications = []
app_tokens = []

def listen_notifications(device_token, email):
    user_result = db_action("read_one", [{"email": email}, "users"], "admin")

    token_list = user_result['device_tokens']
    if device_token not in token_list:
        token_list.append(device_token)
    db_action("update_one", [{"email": email}, {"$set": {"device_tokens": token_list}}, "users"], "admin")

    watchList = db_action("read_one", [{"email_id": email}, "watch_list"], "admin")

    if watchList:
        brands = watchList['brands']
        for brand in brands:
            token_list_result = db_action("read_one", [{"type": brand}, "notif_tokens"], "admin")
            if token_list_result:
                token_list = token_list_result['tokens']
                if device_token not in token_list:
                    token_list.append(device_token)
                db_action("update_one", [{"type": brand}, {"$set": {"tokens": token_list}}, "notif_tokens"], "admin")
            else:
                token_list = [device_token]
                db_action("insert_one", [{"type": brand, "tokens": token_list}, "notif_tokens"], "admin")
        return make_response(jsonify({'message': "Successful", "error": False}), 200)
    else:
        return make_response(jsonify({'message': "Error. No watchlist!", "error": True}), 200)



def add_notification(data):
    notifications.append(data)


def look_for_nots():
    if len(notifications) > 0:
        sendPush("New Notification", json.dumps(notifications[0]), app_tokens)
        db_action("insert_one", [{"time": int(time() * 1000), "data": notifications[0]}, "notifications"], "admin")
        print("Notifications Send")
        notifications.pop(0)


def historical_nots():
    time_filter = int(time() * 1000 - (5 * 24 * 60 * 60 * 1000))
    data = db_action("read_many", [{"time": {"$gte": time_filter}}, "notifications"], "admin")
    opt = []
    for dt in data:
        opt.append([dt['time'], dt['data']])

    for dt in notifications:
        opt.append([int(time() * 1000), dt])

    return {"last 5 days notifications": opt}


