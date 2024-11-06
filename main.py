import requests
from urllib.parse import unquote
from bs4 import BeautifulSoup
from lxml import etree

def collect_data(url: str):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    }

    unquote_url = unquote(url)
    print(unquote_url)
    data = requests.get(url=unquote_url, headers=headers)

    # with open("index.html", "w") as html:
    #     html.write(data.text)

    soup = BeautifulSoup(data.text, "html.parser")
    xml_content = etree.HTML(str(soup))

    op = xml_content.xpath("/html/body/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[3]")
    print(op)


def main():
    collect_data("https://2gis.kz/astana/search/%D0%9A%D0%B0%D1%84%D0%B5?m=71.443176%2C51.130544%2F11.01")


if __name__ == '__main__':
    main()
