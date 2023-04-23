import requests
from bs4 import BeautifulSoup


class HelperService:

    def __check_url_conformity(self, url: str):
        if url:
            conform_url = url[:-1] if url[-1] == '/' else url

            if 'www' in conform_url:
                return conform_url
            else:
                u = conform_url.split('://')
                return '{}://www.{}'.format(u[0], u[1]) if len(u) > 1 else u[0]
        else:
            return ''

    def __iterable_links(self, soup: BeautifulSoup, _url: str):
        val = 'www'
        val_1 = 'http'
        val_2 = 'https'
        lik = '/'

        links = [link.get("href")
                 for link in soup.find_all("a") if link.get("href") != None and val in link.get("href")]
        links_1 = [link.get("href") for link in soup.find_all(
            "a") if link.get("href") != None and val_1 in link.get("href")]
        links_2 = [link.get("href") for link in soup.find_all(
            "a") if link.get("href") != None and val_2 in link.get("href")]

        links_domain = [_url+link.get("href") for link in soup.find_all("a") if link.get("href") != None and val_2 not in link.get(
            "href") if link.get("href") != None and val_1 not in link.get("href") if link.get("href") != None and val not in link.get("href") if link.get("href") != None and lik in link.get("href")]

        return {
            "links": links,
            "links_1": links_1,
            "links_2": links_2,
            "links_domain": links_domain
        }

    def __search_links_in_html(self, data: str, _url: str) -> list[str]:
        soup = BeautifulSoup(data, features="html.parser")

        links_iterable = self.__iterable_links(self, soup, _url)

        links = links_iterable['links']
        links_1 = links_iterable['links_1']
        links_2 = links_iterable['links_2']

        links_domain = links_iterable['links_domain']

        result = [*links, *links_domain, *links_1, *links_2, _url]

        return result

    @classmethod
    def getListLinks(self, data: dict):
        _url = self.__check_url_conformity(self, data["url"])

        try:
            html = requests.get(_url).text
        except Exception as e:
            print(e)
            return []

        return self.__search_links_in_html(self, html, _url)
