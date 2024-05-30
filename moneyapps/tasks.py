from celery import shared_task
import httpx

@shared_task
def fetch_crypto_prices():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {'ids': 'bitcoin', 'vs_currencies': 'usd'}
    response = httpx.get(url, params=params)
    data = response.json()
    return data

@shared_task
def fetch_fiat_rates():
    url = "https://data.fx.kg/api/v1/currencies"
    headers = {'Authorization': 'Bearer xrQq7XzYLGGXvK2ci0X9jhUKRJMvxnFBS9GiLnMAffb77394'}
    response = httpx.get(url, headers=headers)
    data = response.json()
    return data
