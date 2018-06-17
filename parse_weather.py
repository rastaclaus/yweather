#! /usr/bin/python
# pylint: disable=C0103,C0111

import json
from pprint import pprint

with open('weather_data.json', 'r') as json_file:
    wdata = json.load(json_file)

print('температура: {}'.format(wdata.get('fact').get('temp')))
print('давление: {}'.format(wdata.get('fact').get('pressure_mm')))
