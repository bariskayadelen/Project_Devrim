# GET TURKIYE FUEL PRICE

from datetime import datetime
import requests
from bs4 import BeautifulSoup as soup

# Date and Time
today = str(datetime.today().strftime('%Y-%m-%d'))
time = str(datetime.today().strftime("%H:%M:%S"))

fuel_company = "Opet"
url = "https://www.opet.com.tr/akaryakit-fiyatlari/ankara"
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

req = requests.get(url, headers=header)
page_soup = soup(req.content.decode('utf-8','ignore').encode("utf-8"), 'html5lib')
# print(page_soup)
# fuel_district = page_soup.find_all('p', {"class":"Ankara"}).text.strip()
fuel_district = page_soup.find_all('span')
print(fuel_district)
# fuel_price = page_soup.find_all('td', {"data-title":"UNLEADED GASOLINE (TL/LT)"})[0].text.strip()
# diesel_price = page_soup.find_all('td', {"data-title":"TP DIESEL (TL/LT)"})[0].text.strip()
# lpg_price = page_soup.find_all('td', {"data-title":"TPGAS"})[0].text.strip()

# Main function
def main():
    # Table Width
    tbl_len_out = 74
    tbl_len_in = 24

    # Print Currencies and rates
    print(f"\n{' TURKIYE FUEL PRICES ':=^{tbl_len_out}}")
    print(f"\n{' Company':<{tbl_len_in}} : {fuel_company}")
    # print(f"{' City':<{tbl_len_in}} : {fuel_district}")
    print(f"{' Date':<{tbl_len_in}} : {today}")
    print(f"{' Time':<{tbl_len_in}} : {time}")
    # print(f"\n{' Fuel':<{tbl_len_in}} : {fuel_price} ₺")
    # print(f"{' Diesel':<{tbl_len_in}} : {diesel_price} ₺")
    # print(f"{' LPG':<{tbl_len_in}} : {lpg_price} ₺")
    print(f"\n{'':=^{tbl_len_out}}\n")

if __name__ == "__main__":
    main()