import requests
from bs4 import BeautifulSoup

def get_info(soup):
    info = soup.find('table', {'class': 'infobox infobox_v2'}).text
    
    with open(f'{biographic}.txt', 'w') as file:
        file.writelines(info)
        file.close()

def main():
    global biographic
    biographic = input("Digite o nome da pessoa que quer procurar a biografia: ")
    url = f'https://pt.wikipedia.org/wiki/{biographic}'

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        get_info(soup)
    except:
        print('Biografia não encontrada')
        main()

if __name__ == '__main__':
    main()