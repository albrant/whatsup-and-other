import pywhatkit
import requests
from pyfiglet import Figlet
import folium
from functools import lru_cache


@lru_cache()  # кэширование функции, чтобы при повторном вызове не вычислять
def get_info_by_ip(ip='127.0.0.1'):
    """Получаем всю информацию по указанному IP-адресу"""
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        # print(response)

        data = {
            '[IP]': response.get('query'),
            '[int prov]': response.get('isp'),
            '[Org]': response.get('org'),
            '[Country]': response.get('country'),
            '[Region Name]': response.get('regionName'),
            '[City]': response.get('city'),
            '[ZIP]': response.get('zip'),
            '[Lat]': response.get('lat'),
            '[Lon]': response.get('lon'),
        }

        for k, v in data.items():
            print(f'{k} : {v}')

        area = folium.Map(location=[response.get('lat'), response.get('lon')])
        area.save(f'{response.get("query")}_{response.get("city")}.html')

    except requests.exceptions.ConnectionError:
        print('[!] Some trouble with connection')


def send_message_inst():
    """Отправка сообщения через Whatsup
    """
    # mobile = input('Введите номер получателя: ')
    mobile = '+79134445566'
    # message = input('Введите текст сообщения: ')
    message = 'hello, bro'
    pywhatkit.sendwhatmsg_instantly(
        phone_no=mobile,
        message=message,
        wait_time=10,
        tab_close=True,
        close_time=20
    )


def main():
    # from getpass import getpass
    # password = getpass('Введите пароль: ')

    # функция отправки сообщения в Вотсап
    # send_message_inst()

    # создание красивой надписи на экране указанным шрифтом
    preview_text = Figlet(font='slant')
    print(preview_text.renderText('IP INFO'))
    # получение информации по указанному IP
    ip = input('Введите целевой IP: ')
    get_info_by_ip(ip=ip)


if __name__ == '__main__':
    main()
