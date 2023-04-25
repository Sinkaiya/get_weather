#!/usr/bin/python3

import requests


def get_weather():

    locations = {'london': 'Лондон',
                 'cherepovets': 'Череповец',
                 'svo': 'Шереметьево'
                 }

    # URL params format description, just in case: https://wttr.in/:help
    url_main = 'https://wttrr.in/{}?nTQmM&lang=ru'
    url_backup = 'http://wttr.dvmn.org/{}?nTQmM&lang=ru'

    for location in locations.keys():
        try:
            url = url_main.format(location)
            response = requests.get(url)
            response.raise_for_status()
        except requests.exceptions.RequestException:
            url = url_backup.format(location)
            response = requests.get(url)
            response.raise_for_status()

        print(locations[location])
        print()

        line_to_exclude = 'Все новые фичи публикуются здесь: [46m[30m@igor_chubin[0m'
        line_to_replace = '-' * 63
        result = response.text.replace(line_to_exclude, line_to_replace)
        print(result)


get_weather()

# This string is to prevent the terminal window close if that script is being
# run from Windows environment. :)
input('Press ENTER to exit')
