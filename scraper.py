import requests
from bs4 import BeautifulSoup
import re
import smtplib
import time

URL = 'https://www.amazon.com/Dell-Touch-Intel-NVIDIA-GeForce/dp/B07T4HGF79/ref=sr_1_3?keywords=Dell+xps+15&qid=1583106516&sr=8-3'

headers = {"User-Agent": 'Mozilla/i5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}

def find_prize():
    page = requests.get(URL, headers=headers)
    soup1 = BeautifulSoup(page.content,'html.parser')
    soup2 = BeautifulSoup(soup1.prettify(),'html.parser')
    # print(soup.prettify())

    price = soup2.find(id="priceblock_ourprice").get_text()
    price_temp = re.sub("[^\d\.]", "", price)
    price_temp = float(price_temp)

    if(price_temp < 2000):
        send_mail()
    print(price_temp)


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('jeyamaruthi1@gmail.com', 'qysaddaztdymnttq')

    subject = 'Jeyamaruthi, You can afford it !!'
    body = 'Buy it now, do not wait' \
           'also here is the link lazy: https://www.amazon.com/Dell-Touch-Intel-NVIDIA-GeForce/dp/B07T4HGF79/ref=sr_1_3?keywords=Dell+xps+15&qid=1583106516&sr=8-3'

    msg = f"Subject: {subject}\n\n {body}"

    server.sendmail(
        'jeyamaruthi1@gmail.com',
        'jeyamaruthi1@gmail.com',
        msg
    )
    print("Email sent -- ---- -- Successfully!!")

    server.quit()

while(True):
    find_prize()
    time.sleep(60*60*12)