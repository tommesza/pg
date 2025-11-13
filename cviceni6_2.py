import requests
import json


def download_rates(url):
    rates = {}
    response = requests.get(url)
    if not response.ok:
        return None
    data = response.text
    data = data.split("\n")
    data = data[2:]



    for line in data:
        fields = line.split("|")
        if len(fields) < 5:
            continue
        currency = fields[3]
        rate = fields[4]
        rates[currency] = float(rate.replace(",", ".")) / int(fields[2])

    return rates




if __name__ == "__main__":
    url = f"http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt"

    rates = download_rates(url)
    print(rates)