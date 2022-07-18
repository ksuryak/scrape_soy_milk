import selectorlib
from selectorlib import Extractor
import requests
import json
from time import sleep
from fake_useragent import UserAgent


# Create an Extractor by reading from the YAML file
e = Extractor.from_yaml_file('soymilk_attr.yml')


def scrape(url):
    ua = UserAgent()
    #  Standard headers to pass through the webpage auth
    headers = {
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': ua.random,
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.amazon.com/',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    # Download the page using requests
    print("Downloading %s" % url)
    r = requests.get(url, headers=headers)
    # Simple check to check if page was blocked (Usually 503)
    if r.status_code > 500:
        if "To discuss automated access to Amazon data please contact" in r.text:
            print(
                "Page %s was blocked, use alternate proxy\n" % url)
        else:
            print("Page %s must have been blocked by Amazon as the status code was %d" % (
                url, r.status_code))
        return None
    # Pass the HTML of the page and create
    print(e.extract(r.text))
    return e.extract(r.text)


# product_data = []
with open("Soy_Milk_Url.txt", 'r') as urllist, open('search_output_review.jsonl', 'w') as outfile:
    f = open('product_urls.txt','a+')
    for url in urllist.read().splitlines():
        data = scrape(url)

       
        if data:
            try:
                for product in data['product']:
                    product['url'] = 'https://www.amazon.com' + product['url']
                    f.write(product['url'])
                    f.write('\n')

                    json.dump(product, outfile)
                    outfile.write(", \n")
                    # sleep(5)
                
            except:
                continue
    f.close()