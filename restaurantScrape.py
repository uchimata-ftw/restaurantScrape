#! /usr/bin/python3

import bs4, requests, os, pyperclip, csv

#get webPage address go scrape from clipboard

address = pyperclip.paste();

res = requests.get(address)

res.raise_for_status()

#formats web Page
page = bs4.BeautifulSoup(res.text, "lxml")
page.prettify()
type(page)

#scrapes for restaurant page and writes to csv file
nameArray = []
for span in page.find_all("a", "biz-name"):
        page.strippedstrings
        nameArray.append(span.text)

#scrapes for addresses and writes to csv file
addressArray = []
for address in page.find_all("address"):
        page.strippedstrings
        addressArray.append(address.text)

#scrapes for phone numbers and writes to csv file
phoneArray = []
for span in page.find_all("span", "biz-phone"):
        page.strippedstrings
        phoneArray.append(span.text)

#writes list to file called restaurant.csv
f = open('restaurant.csv', 'a')
for i in range(len(nameArray)):
        f.write(nameArray[i] + "\n")
f.close()

f = open('phone.csv', 'a')
for i in range(len(phoneArray)):
        f.write(phoneArray[i] + "\n")
f.close()

f = open('address.csv', 'a')
for i in range(len(addressArray)):
        f.write(addressArray[i] + "\n")
f.close()
