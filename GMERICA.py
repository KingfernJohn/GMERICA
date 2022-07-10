from msilib import UuidCreate
from bs4 import BeautifulSoup
import requests, os, time, uuid
from datetime import datetime

url = "https://gme.crazyawesomecompany.com"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

table = soup.find("table",attrs={"class":"table"})
rows = table.find_all("tr")
td = table.find_all("td")
td = td[:7]
td = str(td)
td = td[5:]
gme_date = td.partition("<")[0]
gme_available = td.partition('d">')[2].partition("</td>")[0]
td = td[td.find('<td>'):]
td = td[4:]
gme_fee = td.partition("<")[0]

table2 = soup.find("div",attrs={"class":"col-12 mt-3"})
h1 = table2.find_all("h1")
h1 = str(h1)
h1 = h1[22:]
gme_locked_perc = h1.partition("<")[0]

p = table2.find_all("p")
p = str(p)
p = p[128:]
gme_locked_shares = p.partition(" s")[0]
p = table2.find_all("p")
p = str(p)
p = p[205:]
gme_remaining_shares = p.partition(" s")[0]

url = "https://www.marketwatch.com/investing/stock/gme"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

table = soup.find("ul",attrs={"class":"list list--kv list--col50"})
rows = table.find_all("li")
f_row = rows[0]
f_row = str(f_row)
d_row = rows[3]
d_row = str(d_row)
f_row = f_row[78:]
d_row = d_row[84:]
gme_open_price = f_row.partition("</s")[0]
gme_market_cap = d_row.partition("</s")[0]

table = soup.find("h2",attrs={"class":"intraday__price"})
rows = table.find_all("bg-quote")
m_row = rows[0]
m_row = str(m_row)
m_row = m_row[150:]
gme_current_price = m_row.partition("</bg-")[0]
gme_current_price = "$"+gme_current_price

table = soup.find("div",attrs={"class":"element element--intraday"})
rows = table.find_all("div")
g_row = rows[4]
g_row = str(g_row)
g_row = g_row[329:]
gme_close_price = g_row.partition(" </td>")[0]

os.system('cls')
today = time.strftime("%a, %d %b %Y")
now = time.strftime("%H:%M:%S")
gme_fee_flo = gme_fee[:4]
gme_fee_flo = float(gme_fee_flo)
gme_current_price_float = gme_current_price[1:]
gme_current_price_float = float(gme_current_price_float)
rndm_uuid = uuid.uuid4()
rndm_uuid = str(rndm_uuid)
data = open("Saves/"+rndm_uuid+"_$GME_"+".txt", "w+")
gme_news = f"{today}\n{now}\n\n$GME - Update\n\n{gme_current_price} Current Price\n{gme_close_price} Closing Price\n{gme_market_cap} Market Cap\n\n{gme_locked_perc} / {gme_locked_shares} are locked -> {gme_remaining_shares} left\n\n{gme_date} -> {gme_available} Shares avaible with {gme_fee} Fee\n\nCost of one Short =~ ${round(gme_fee_flo/100*gme_current_price_float+gme_current_price_float,2)}\n\n\n"
print(gme_news)
data.write(gme_news)
data.close()
quit()