## Scrapping the website coinmarketcap.com 
This Django project scrap the site for the given coin and get a jobIds for each coin and than get the data from the job id recived previously

## Setup
- Install all the library
```
pip install -r requirements.txt
```
- run the celery worker
```
celery -A scrapcoin worker --beat -l info
```
- for celery to work you need redis so i have given a docker-compose file to setup redis just run the command and add url in env file
```
docker-compose up
```
##### url :- CELERY_BROKER_REDIS_URL=redis://localhost:6379
- Now for the Django do this commands
```
python3 manage.py makemigrations
python3  manage.py migrate
python3 manage.py runserver
```
Now you are ready to use it 
## API Endpoints
- start scraping and get the jobId
 ![postman_sc_intern](https://github.com/Aryangp/scraping_coin_market_ignis_tech_intern/assets/91003905/bc60806b-c6ac-49c6-8049-83d3c208ac79)
- To get the data from job id
![postman_sc_intern1](https://github.com/Aryangp/scraping_coin_market_ignis_tech_intern/assets/91003905/714a8f44-f03b-4734-8068-cbe138840247)



## Screenshot of Admin Panel

![internship_scrap2](https://github.com/Aryangp/scraping_coin_market_ignis_tech_intern/assets/91003905/4d8f9449-4c96-4559-b36c-eceea508e925)

![internship_scrap3](https://github.com/Aryangp/scraping_coin_market_ignis_tech_intern/assets/91003905/5e36f47f-b3f9-42c4-81dd-3841f7b6aed8)

![internship_scrap4](https://github.com/Aryangp/scraping_coin_market_ignis_tech_intern/assets/91003905/0dc2af6b-56de-4061-943d-2bed15770369)

![internship_scrap5](https://github.com/Aryangp/scraping_coin_market_ignis_tech_intern/assets/91003905/a89c3942-32ca-483f-9fc0-7c113fc12d8b)

![internship_scrap7](https://github.com/Aryangp/scraping_coin_market_ignis_tech_intern/assets/91003905/c8cffe9b-a94d-4aaf-a353-8e9edb785d7a)

![internship_scrap6](https://github.com/Aryangp/scraping_coin_market_ignis_tech_intern/assets/91003905/f2fed7ef-e962-4327-8c32-bb697b689476)

![internship_scrap8](https://github.com/Aryangp/scraping_coin_market_ignis_tech_intern/assets/91003905/2c01a695-63e8-446c-babe-8ca6aeca49df)

![internship_scrap9](https://github.com/Aryangp/scraping_coin_market_ignis_tech_intern/assets/91003905/80657d0c-8302-4fbf-a693-e70463566dba)




