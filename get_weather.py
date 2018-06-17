#! /usr/bin/python
# pylint: disable=C0103,C0111

from pprint import pprint
import json
import requests

url = 'https://api.weather.yandex.ru/v1/forecast'

params = {
    'lat': 55.7539,
    'lon': 37.620393,
    'extra': True,
    'lang': 'ru_RU'}

headers = {
    'X-Yandex-API-Key': 'fbe79d80-71cd-4433-b2e8-94bc2456c522'
}

resp = requests.get(url, params=params, headers=headers)

weather_json = json.loads(resp.content.decode())
with open('weather_data.json', 'w') as json_file:
    json.dump(weather_json, json_file)
