import requests
from pyfiglet import Figlet


def get_info_by_ip(ip):
     try:
         response = requests.get(url=f'http://ip-api.com/json/{ip}').json()

         data = {
            '[IP]': response.get('query'),
            '[Country]': response.get('country'),
            '[City]': response.get('city'),
            '[Lat]': response.get('lat'),
            '[Lon]': response.get('lon'),
         }

         for k, v in data.items():
            print(f'{k} : {v}')
     except requests.exceptions.ConnectionError:
         print('[!] Please check your connection')


def main():
    preview_text = Figlet(font='slant')
    print(preview_text.renderText('IP INFO'))
    ip = input('Please enter a target IP: ')

    get_info_by_ip(ip)


if __name__ == '__main__':
    main()