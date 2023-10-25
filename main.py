
from get_users import *


def main():
    # url_root = "https://card.wb.ru/cards/v1/detail?appType=1&curr=rub&dest=-1257786&regions=80,83,38,4,64,33,\
    #             68,70,30,40,86,75,69,1,66,110,22,48,31,71,112,114&spp=29&nm=180000436;145477842;165289636;170609383;\
    #             170609385;175633601;175633602;175633603;175633604;175633605;180000433;180000437;180000441;180000442;\
    #             180000444;180000446;180000448;180012497;\
    #             180012499;180012501;180012508;181363455;180012509;180000440;180012510;180000438;180012502;180000430"

    # json_pos = get_jsone(url_root)
    # products = json_pos["data"]["products"]
    # root_id = list(get_root(products))
    # print(root_id)

    lst_price = [
        "https://feedbacks2.wb.ru/feedbacks/v1/160431339",
        "https://feedbacks1.wb.ru/feedbacks/v1/114577144",
        "https://feedbacks1.wb.ru/feedbacks/v1/159298606"
    ]
    lst_time_otz = []
    for i in lst_price:
        respons = get_jsone(i)
        users = get_user_coment_dict(respons)
        sort_us = sort_users_lst(users)
        dl_c = del_coment(sort_us)
        sr_a = sr_arefm(dl_c)
        lst_time_otz.append(sr_a)

    result = sum(lst_time_otz) / len(lst_time_otz)
    return (f"Шарф палантин осенний зимний кашемир: {lst_time_otz[0]:.2f}\n\nНожницы маникюрные: "
            f"{lst_time_otz[1]:.2f}\n\nЗонт автомат антиветер однотонный черный: {lst_time_otz[2]:.2f}\n\n"
            f"Среднее время между отрицательным и следующим положительным отзывом: {result:.2f} мин.")

