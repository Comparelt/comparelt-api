from bs4 import BeautifulSoup
import requests
import json


class CrawlingService:
    def __init__(self):
        return

    def crawl(search_input):
        search_query = search_input.replace(" ", '+')
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}

        # =========== GOOGLE SHOPPING ===========
        try:
            link_google = 'https://www.google.com/search?q=' + search_query + '&rlz=1C5CHFA_enKR893KR893&biw=1280&bih=689&tbm=shop&sxsrf=AOaemvJ5m8WvwuNJE78HxodXTvD6wLXzCg%3A1632900081294&ei=8RNUYauXEfS-3LUPyb6EGA&oq=adidas+yeezy&gs_lcp=Cgtwcm9kdWN0cy1jYxADMgQIIxAnMgQIIxAnMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyCAgAEIAEEIsDMggIABCABBCLAzIICAAQgAQQiwM6BAgAEBhQoBVYoBVgkxhoAHAAeACAAY4CiAHxBJIBBTAuMi4xmAEAoAEBuAEBwAEB&sclient=products-cc&ved=0ahUKEwjr07Hq0qPzAhV0H7cAHUkfAQMQ4dUDCAs&uact=5'
            source_google = requests.get(link_google).text

            soup_google = BeautifulSoup(source_google, 'lxml')

            item_google = soup_google.find('div', class_='KZmu8e')
            title_google = item_google.find(
                'div', class_='sh-np__product-title translate-content').text
            picture_google = item_google.img['src']
            # a_google = item_google.find('a', class_='shntl sh-np__click-target')['href']
            a_google = item_google.find('a')['href']
            price_google = item_google.find('b', class_='translate-content').text
        except:
            title_google = "N/A"
            picture_google = "N/A"
            a_google = "N/A"
            price_google = "N/A"

        # =========== COUPANG ===========
        link_coupang = 'https://www.coupang.com/np/search?component=&q=' + \
            search_query + '&channel=user'
        source_coupang = requests.get(link_coupang, headers=headers)
        source_coupang.raise_for_status()
        soup_coupang = BeautifulSoup(source_coupang.text, 'lxml')

        # gets the second item from the product list because the first one is always an ad and may not be the product searched
        item_coupang = soup_coupang.find(
            'ul', {"id": "productList"}).find_all('li')[1]
        title_coupang = item_coupang.find('div', class_='name').text
        picture_coupang = item_coupang.img['src']
        a_coupang = 'http://coupang.com' + \
            item_coupang.find('a', class_='search-product-link')['href']
        price_coupang = item_coupang.find('strong', class_='price-value').text

        # =========== SSG ===========
        search_query_ssg = search_input.replace(" ", '%20')
        link_ssg = 'http://www.ssg.com/search.ssg?target=all&query=' + \
            search_query_ssg

        source_ssg = requests.get(link_ssg, headers=headers).text

        soup_ssg = BeautifulSoup(source_ssg, 'lxml')

        item_coupang = soup_coupang.find(
            'ul', {"id": "productList"}).find_all('li')[1]

        item_ssg = soup_ssg.find('ul', {"id": "idProductImg"}).find('li')
        title_ssg = item_ssg.find('em', class_='tx_en').text
        picture_ssg = item_ssg.img['src']
        a_ssg = 'http://www.ssg.com/' + \
            item_ssg.find('div', class_='cunit_info').find('a')['href']
        price_ssg = item_ssg.find('div', class_='cunit_price notranslate').find(
            'em', class_='ssg_price').text

        data = [
            {
                "title": title_google,
                "picture": picture_google,
                "link": a_google,
                "price": price_google
            },
            {
                "title": title_coupang,
                "picture": picture_coupang,
                "link": a_coupang,
                "price": price_coupang
            },
            {
                "title": title_ssg,
                "picture": picture_ssg,
                "link": a_ssg,
                "price": price_ssg
            },
        ]

        return json.dumps(data, indent=4)
