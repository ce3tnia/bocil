import re
import pandas as pd
import urllib.request as urllib2
from bs4 import BeautifulSoup
from tabulate import tabulate
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

quote_page = 'https://www.scimagojr.com/journalrank.php?country=ID'
page = urllib2.urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')
table = soup.find_all('table', attrs={'':''})

cleanr = re.compile('<.*?>')
hasil = []
for tbl in table:
    clean = re.sub(cleanr, '', str(tbl))
    hasil.append(clean)

text = """
Ranking Jurnal Indonesia
{table}
"""
html = """\
<html>
  <head>
    <style>
      table, th, td, tr{{border: 1px solid black; border-collapse: collapse;}}
      th, td, tr {{padding: 5px;}}
      p {{font-weight: bold; color: black;}}
    </style>
  </head>
  <body>
    <p>Ranking Jurnal Indonesia</p>
    {table}
  </body>
</html>
"""

data = pd.read_html(str(table))
text = text.format(table=tabulate(data[0], headers='keys', tablefmt='grid', numalign='center'))
html = html.format(table=tabulate(data[0], headers='keys', tablefmt='html', numalign='center'))
message = MIMEMultipart(
  'alternative', None, [MIMEText(text), MIMEText(html, 'html')])
# dhasil = tabulate(hasil[0], headers='keys', tablefmt='fancy_grid', numalign='center')

#email credentials
sender_email = 'keziabtr84@gmail.com'
receive_email = 'ceciliatania03@gmail.com'
password = 'Nabilah1111'

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(sender_email, password)

# msg = ('Subject: Ranking Jurnal Indonesia\n\n\
# {}\n'.format(dhasil))
message['Subject'] = 'Ranking Jurnal Indonesia'
message['From'] = sender_email
message['to'] = receive_email
server.sendmail(sender_email, receive_email, message.as_string())
print('Email sent!')