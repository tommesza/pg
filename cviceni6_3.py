import sys
from cviceni6_2 import download_rates

def convert(ammount_czk):
    result = {}
    
    rates = download_rates("http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt")
    
    for code, rate in rates.items():
        result[code] = ammount_czk / rate


    return result




if __name__ == "__main__":


    ammount_czk = int(sys.argv[1])

    conversions = convert(ammount_czk)

    for cur, cur_ammount in conversions.items():
        print(cur, cur_ammount)