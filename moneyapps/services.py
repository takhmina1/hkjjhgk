# import httpx
# from .models import Currency, ExchangeRate
# from django.utils import timezone

# class ExchangeService:
#     async def fetch_and_save_currencies(self):
#         url = "https://data.fx.kg/api/v1/currencies"
#         headers = {
#             'Authorization': 'Bearer xrQq7XzYLGGXvK2ci0X9jhUKRJMvxnFBS9GiLnMAffb77394'
#         }

#         async with httpx.AsyncClient() as client:
#             try:
#                 response = await client.get(url, headers=headers)
#                 response.raise_for_status()  # Проверка на наличие ошибок
#                 data = response.json()

#                 for currency_data in data:
#                     currency, created = Currency.objects.get_or_create(
#                         code=currency_data['code'],
#                         defaults={'name': currency_data['name']}
#                     )

#                     ExchangeRate.objects.create(
#                         currency=currency,
#                         rate=currency_data['rate'],
#                         timestamp=timezone.now()
#                     )

#                 print("Data saved successfully.")

#             except httpx.HTTPStatusError as e:
#                 print(f"HTTP error occurred: {e.response.status_code} - {e.response.text}")
#             except httpx.RequestError as e:
#                 print(f"Request error occurred: {str(e)}")
#             except Exception as e:
#                 print(f"An error occurred: {str(e)}")

#     async def fetch_and_save_bitcoin_rate(self):
#         url = "https://api.coingecko.com/api/v3/simple/price"
#         params = {
#             'ids': 'bitcoin',
#             'vs_currencies': 'usd'
#         }

#         async with httpx.AsyncClient() as client:
#             try:
#                 response = await client.get(url, params=params)
#                 response.raise_for_status()  # Проверка на наличие ошибок
#                 data = response.json()

#                 bitcoin_currency, created = Currency.objects.get_or_create(
#                     code='BTC',
#                     defaults={'name': 'Bitcoin'}
#                 )

#                 ExchangeRate.objects.create(
#                     currency=bitcoin_currency,
#                     rate=data['bitcoin']['usd'],
#                     timestamp=timezone.now()
#                 )

#                 print("Data saved successfully.")

#             except httpx.HTTPStatusError as e:
#                 print(f"HTTP error occurred: {e.response.status_code} - {e.response.text}")
#             except httpx.RequestError as e:
#                 print(f"Request error occurred: {str(e)}")
#             except Exception as e:
#                 print(f"An error occurred: {str(e)}")








import httpx
from .models import Currency, ExchangeRate
from django.utils import timezone

class ExchangeService:
    async def fetch_and_save_currencies(self):
        url = "https://data.fx.kg/api/v1/currencies"
        headers = {
            'Authorization': 'Bearer xrQq7XzYLGGXvK2ci0X9jhUKRJMvxnFBS9GiLnMAffb77394'
        }

        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(url, headers=headers)
                response.raise_for_status()  # Проверка на наличие ошибок
                data = response.json()

                for currency_data in data:
                    currency, created = Currency.objects.get_or_create(
                        code=currency_data['code'],
                        defaults={'name': currency_data['name']}
                    )

                    ExchangeRate.objects.create(
                        currency=currency,
                        rate=currency_data['rate'],
                        timestamp=timezone.now()
                    )

                print("Data saved successfully.")

            except httpx.HTTPStatusError as e:
                print(f"HTTP error occurred: {e.response.status_code} - {e.response.text}")
            except httpx.RequestError as e:
                print(f"Request error occurred: {str(e)}")
            except Exception as e:
                print(f"An error occurred: {str(e)}")

    async def fetch_and_save_bitcoin_rate(self):
        url = "https://api.coingecko.com/api/v3/simple/price"
        params = {
            'ids': 'bitcoin',
            'vs_currencies': 'usd'
        }

        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(url, params=params)
                response.raise_for_status()  # Проверка на наличие ошибок
                data = response.json()

                bitcoin_currency, created = Currency.objects.get_or_create(
                    code='BTC',
                    defaults={'name': 'Bitcoin'}
                )

                ExchangeRate.objects.create(
                    currency=bitcoin_currency,
                    rate=data['bitcoin']['usd'],
                    timestamp=timezone.now()
                )

                print("Data saved successfully.")

            except httpx.HTTPStatusError as e:
                print(f"HTTP error occurred: {e.response.status_code} - {e.response.text}")
            except httpx.RequestError as e:
                print(f"Request error occurred: {str(e)}")
            except Exception as e:
                print(f"An error occurred: {str(e)}")
