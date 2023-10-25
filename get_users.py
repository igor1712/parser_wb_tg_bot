from datetime import timedelta
import requests
import json
from datetime import datetime


def get_jsone(url):

    heders = {"User-Agent": "Mozill/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                            "(KHTML, like Gecko) Chrome/116.0.5845.967 YaBrowser/23.9.1.967 Yowser/2.5 Safari/537.36}"}

    response = requests.get(url, headers=heders).text
    return json.loads(response)


def get_root(products):
    ids = set()
    for item in products:
        ids.add(item["root"])
    return ids


def get_user_coment_dict(data):


    len_data = len(data["feedbacks"])
    user_data = data["feedbacks"]
    users = []
    for item in range(len_data):
        data_all = user_data[item]["createdDate"].split("T")
        data = list(map(int, data_all[0].split("-")[::-1]))
        time = list(map(int, data_all[1].split(":")[:2]))
        time[0] += 3  #"костыль почему то без него время на 3 часа отстает"
        star = user_data[item]["productValuation"]
        name = user_data[item]["wbUserDetails"]["name"]
        text = user_data[item]["text"]
        users.append({
            "star" : star,
            "data" : data,
            "time" : time,
            "name" : name
        })
    return users


def sort_users_lst(lst):
    lst = sorted(lst, key=lambda d: (d['data'][1], d["data"][0], d["time"][0], d["time"][1]), reverse=True)
    return lst


def del_coment(my_dict):
    dt = int(str(datetime.now()).split(" ")[0].split("-")[1])
    data_mes = []
    for i in my_dict:
         if i["data"][1] is dt:
            data_mes.append(i)
    return data_mes


def sr_arefm(reviews):
    reviews.sort(key=lambda r: (r['data'], r['time']))

    total_diff = 0
    count = 0
    negative_review_time = None

    for review in reviews:
        review_time = datetime(day=review['data'][0], month=review['data'][1], year=review['data'][2],
                               hour=review['time'][0] % 24, minute=review['time'][1]) + timedelta(
            days=review['time'][0] // 24)
        if 1 <= review['star'] <= 3:
            negative_review_time = review_time
        elif 4 <= review['star'] <= 5 and negative_review_time is not None:
            diff = review_time - negative_review_time
            total_diff += diff.total_seconds() / 60
            count += 1
            negative_review_time = None

    if count > 0:
        average_time = total_diff / count
        return average_time
    else:
        return ("Нет положительного отзыва после отрицательного.")