import requests
from bs4 import BeautifulSoup


def parses():
    html = requests.get("https://free-proxy-list.net/anonymous-proxy.html")
    html = html.text
    parse = BeautifulSoup(html, "lxml")
    table = parse.find("table", id="proxylisttable").find("tbody").find_all("tr")
    proxy = []
    for tr in table:
        td = tr.find_all("td")
        ip_and_proxy = td[0].text + ":" + td[1].text
        proxy.append(ip_and_proxy)
    _proxy=str(proxy)
    _proxy=_proxy.replace("[", ""); _proxy=_proxy.replace("]", ""); _proxy=_proxy.replace("'", "")
    _proxy=_proxy.replace(",", ""); _proxy=_proxy.replace(" ", "\n")
    with open("proxy.txt", 'w+') as f:
        f.write(_proxy)

