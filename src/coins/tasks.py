from celery import shared_task
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import json
import uuid
from .models import Job, Task, Output, Contract, OfficialLink, Social

"""
This file has the task that celery will do for the scraping of the data from the website
here we are using selenium to scrape the data from the website I am getting the data and putting it in 
python dictionary and then saving it in the database models that are created in models.py

Note:- I was unable to get the url of twitter and telegram so I have put the hardcoded url in the socials
as i tried but it always returned a url to download a app of this site i just wanted to clearlify this


"""



@shared_task
def scrape_coin_data(job_id,coinNeed):
    options=ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument('--remote-debugging-pipe')
    # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    '''
    getting all the data here for the coin and value 
    '''
    with webdriver.Chrome(options=options) as driver:
        url = f"https://coinmarketcap.com/currencies/{coinNeed}/"
        driver.get(url)
        price =driver.find_element(By.XPATH, "//span[contains(@class,'fsQm')]").text
        pricePrecentage=driver.find_element(By.XPATH,"//p[contains(@class,'iPawMI')]").text
        allCap= driver.find_elements(By.XPATH, '//dd')
        typeCoin=driver.find_element(By.XPATH,"//span[contains(@class,'dEZnuB')]").text  #eESYbg 
        codeCoin=driver.find_element(By.XPATH,"//span[contains(@class,'eESYbg')]").text
        websiteLinks=driver.find_element(By.XPATH, "//a")
        maketCap=allCap[0].text.split("\n")
        volume=allCap[1].text.split("\n")
        circulatingSupply=allCap[2].text
        totalSupply=allCap[3].text
        dilutedMarketCap=allCap[4].text
        fullyDilutedMarketCap=allCap[5].text
        mainLink=websiteLinks.get_attribute('href')


    # Prepare the output in the desired format
    data = {
        "coin": coinNeed,
        "output": {
            "price": price,
            "price_change": pricePrecentage,
            "market_cap": maketCap[0],
            "market_change": maketCap[1],
            "volume": volume[0],
            "volume_change": volume[1],
            "circulating_supply": circulatingSupply,
            "total_supply": totalSupply,
            "diluted_market_cap": dilutedMarketCap,
            "contracts": [
                {
                    "name": typeCoin,
                    "address": codeCoin
                }
            ],
            "official_links": [
                {
                    "name": "website",
                    "link": mainLink
                }
            ],
            "socials": [
                {
                    "name": "twitter",
                    "url": "https://twitter.com/dukocoin"
                },
                {
                    "name": "telegram",
                    "url": "https://t.me/+jlScZmFrQ8g2MDg8"
                }
            ]
        }
    }
    print(data)
            # Add more tasks for other coins here...
    job = Job.objects.get(pk=job_id)
    task = Task.objects.create(job=job, coin=data['coin'])

    output_data = data['output']
    output = Output.objects.create(
        task=task,
        price=output_data['price'],
        price_change=output_data['price_change'],
        market_cap=output_data['market_cap'],
        market_change=output_data['market_change'],
        volume=output_data['volume'],
        volume_change=output_data['volume_change'],
        circulating_supply=output_data['circulating_supply'],
        total_supply=output_data['total_supply'],
        diluted_market_cap=output_data['diluted_market_cap'],
    )

    for contract_data in output_data['contracts']:
        Contract.objects.create(output=output, name=contract_data['name'], address=contract_data['address'])

    for link_data in output_data['official_links']:
        OfficialLink.objects.create(output=output, name=link_data['name'], link=link_data['link'])

    for social_data in output_data['socials']:
        Social.objects.create(output=output, name=social_data['name'], url=social_data['url'])

    return f"Job {job_id} completed"        
        