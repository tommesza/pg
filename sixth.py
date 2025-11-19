import sys
import requests

def download_url_and_get_all_hrefs(url):
    hrefs = []

    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Nepodarilo se stahnout stranku")

    html = response.text

    pos = 0
    while True:
        start = html.find('href="', pos)
        if start == -1:
            break

        start = start + 6  # přeskočíme 'href="'
        end = html.find('"', start)
        if end == -1:
            break

        link = html[start:end]
        hrefs.append(link)

        pos = end + 1

    return hrefs


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        links = download_url_and_get_all_hrefs(url)
        for l in links:
            print(l)
    except Exception as e:
        print("Program skoncil chybou:", e)
