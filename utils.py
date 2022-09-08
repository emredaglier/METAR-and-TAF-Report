import requests
import re
import time

def _checkInput(ICAO):
    if len(ICAO) == 4:
        if ICAO.isalpha():
            return True
    return False

def _getWeatherData(ICAO):

    if _checkInput(ICAO):
        URL = f'https://www.aviationweather.gov/metar/data?ids={ICAO}&format=raw&date=&hours=0&taf=on' #Get URL

    else:
        return 0

    try:
        # Bring the HTML data to string and gather 
        # METAR and TAF data

        page = requests.get(URL)

        first = [m.start() for m in re.finditer('<code>', page.text)]
        last = [m.start() for m in re.finditer('</code>', page.text)]

        METAR = page.text[first[0] + 6:last[0]]
        TAF = page.text[first[1] + 6:last[1]]

        while True:
            if '<br/>&nbsp;&nbsp;' in TAF:
                TAF = TAF[:TAF.find('<br/>&nbsp;&nbsp;')] + TAF[TAF.find('<br/>&nbsp;&nbsp;') + 17:]
            else:
                break

        return METAR, TAF

    except requests.exceptions.ConnectionError: #If there's no connection established, return -1
        return -1

    except IndexError:
        return -2

def _getUTC():
    return time.strftime('%H%M', time.gmtime())

def _getUTCGap(METAR):
    UTC = _getUTC()
    UTC_HRS, UTC_MINS = UTC[:2], UTC[2:]

    METAR_UTC = METAR[7:11]
    METAR_UTC_HRS, METAR_UTC_MINS = METAR_UTC[:2], METAR_UTC[2:]

    gap = (str(int(UTC_HRS) - int(METAR_UTC_HRS)), str(int(UTC_MINS) - int(METAR_UTC_MINS)))

    return gap


def parseData(ICAO):
    PHOLDER = _getWeatherData(ICAO)
    if PHOLDER == 0: return 0
    if PHOLDER == -1: return -1
    if PHOLDER == -2: return -2

    METAR, TAF = PHOLDER
    GAP = _getUTCGap(METAR)

    return (METAR, TAF), GAP
