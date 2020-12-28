import requests
from lxml import html
import os

# print("URL : ")
# url = input()
url = "https://news.google.com"
response = requests.get(url)

if response.status_code == 200:
    print("Response ok!")
    page = html.fromstring(response.text)
    # text = page.cssselect("a.DY5T1d.RZIKme")[0].text
    # print(text)

    f = open("titles.txt", "w")
    for a in page.cssselect("a.DY5T1d.RZIKme"):
        f.write(str(a.text_content().encode("utf-8")) + os.linesep)
        # print()

    f.close()
else:
    print("Request failed")
