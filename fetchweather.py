import pycountry
from newsapi import NewsApiClient
newsapi=NewsApiClient(api_key='fc71c0c1d9d64fa3b449e26e1c5afd08')
input_country =input("Enter Country...")
input_countries=[f'{input_country.strip()}']
countries={}

for country in pycountry.countries:
    countries[country.name]=country.alpha_2
codes=[countries.get(country.title(),'Unknown Code') for country in input_countries]

option = input("Which category are you interested in?\n1.Business\n2.Entertainment\n3.General\n4.Health\n5.Science\n6.Technology\n\nEnter your desired category: ")

top_headlines=newsapi.get_top_headlines(category=f'{option.lower()}', language='en', country=f'{codes[0].lower()}')
Headlines=top_headlines['articles']

if Headlines:
    for articles in Headlines:
        b=articles['title'][::-1].index("-")
        if "news" in (articles['title'][-b+1:]).lower():
            print(f"{articles['title'][-b+1:]}: {articles['title'][:-b-2]}.")
        else:
            print(f"{articles['title'][-b+1:]} News: {articles['title'][:-b-2]}.")
else:
    print(f"No news in {codes[0].lower()}.")
