from unidecode import unidecode
import requests
from bs4 import BeautifulSoup
import numpy as np
from datetime import date
import smtplib

def bs4_all_desire_element(url, elements_1, elements_2):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.find_all(elements_1, class_=elements_2)
    return elements

def get_specific_element(url, elements_1, elements_2, numero_posicion_elemento):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.find_all(elements_1, class_=elements_2)
    return elements[numero_posicion_elemento].get_text()

def all_links(url, linktext_or_links_or_dictlinks):

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')

    keys = []
    values = []
    for link in links:

        keys.append(link.string)
        values.append(link.get('href'))

    dict_all_links = dict(zip(keys, values))


    if linktext_or_links_or_dictlinks == "linktext":

        return list(dict_all_links.keys())

    elif linktext_or_links_or_dictlinks == "links":

        links = list(set(list(dict_all_links.values())))
        all_unique_links = []

        for link in links:

            try:
                if not ("www." in link or "https" in link):

                    all_unique_links.append(url + link)

                else:
                    all_unique_links.append(link)

            except:
                pass


        return all_unique_links

    elif linktext_or_links_or_dictlinks == "dictlinks":

        return dict_all_links



def all_links_on_webpage(url):

    starter_links = all_links(url, "links")
    all_unique_links = []

    while True:

        for link in starter_links:

            if url not in link:
                all_unique_links.append(link)

            else:

                all_unique_links.extend(all_links(link, "links"))

                set(all_unique_links)

                print(all_unique_links)


    starter_links = list(set(starter_links + all_unique_links))

    print(starter_links)



def main():


    all_links_on_webpage("https://www.eleconomista.es/")


if __name__ == '__main__':
    main()


