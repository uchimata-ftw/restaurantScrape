#! /usr/bin/python3

import bs4, requests, os, sys, pyperclip, csv

#get webPage address go scrape from command line or clipboard

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])

else:
    address = pyperclip.paste();

res = requests.get(address)

res.raise_for_status()

page = bs4.BeautifulSoup(res.text, "lxml")
page.prettify()
type(page)

baconFile = open('restaurant.txt', 'w',)
for span in page.find_all("a", "biz-name"):
        page.strippedstrings
        baconFile.write(span.text + "\n")

baconFile.close()
        

