# import requests
# from bs4 import BeautifulSoup

# url = 'https://www.akchabar.kg/ru/'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'lxml')
# block = soup.find('ul', class_='list-inline')

# usd = block.text.index("E")
# usd_text = block.text[0:usd]
# usd_text = usd_text[:3] + ' ' + usd_text[3:]

# eur = block.text.index("RU" )
# eur_text = block.text[usd:eur]
# eur_text = eur_text[:3] + ' ' + eur_text[3:]

# rub = block.text.index("KZ")
# rub_text = block.text[eur:rub]
# rub_text = rub_text[:3] + ' ' + rub_text[3:]

# kzt_text = block.text[rub:]
# kzt_text = kzt_text[:3] + ' ' + kzt_text[3:]

# all = [usd_text, eur_text, rub_text, kzt_text]

# # usd_text, eur_text, rub_text, kzt_text

id = 2

a = [[1,2], [2,3]]
counter = [1,2,3,4]

for x in a:
    print(x)
    if counter == id:
        print(x)
        for i in x:
            print(i)
