#Error Codes
# 0: Invalid input (numbers or special characters in ICAO code etc.)
# 1: No internet connection
# 2: Invalid airport (No such airport named given ICAO)

from utils import parseData
import os

def cls():
    os.system('cls')

if __name__ == '__main__':
    while True:
        cls()
        print('Airport Weather Information Based on NOAA')
        print('Enter 0 to exit.\n')

        ICAO = input('ICAO:\t')
        if ICAO == '0': exit()

        data = parseData(ICAO)

        cls()
        if data == 0:
            print('You have ented invalid input (Possibly invalid characters). Press Enter to try again.')
            input()

        if data == -1:
            print('No internet connection has been established, please check your connection. Press Enter to try again.')
            input()

        if data == -2:
            print(f'{ICAO.upper()} is an invalid airport. Press Enter to try again.')
            input()

        print(f'METAR: {data[0][0]}')
        print(f'TAF: {data[0][1]}\n')

        if data[1][0] == '0':
            print(f'This weather data has been published {data[1][1]} minutes ago')
        
        else:
            print(f'This weather data has been published {data[1][0]} hours {data[1][0]} minutes ago')
        
        print('\nEnter 0 to exit.')
        a = input()

        if a == '0': exit()
        

        

            


