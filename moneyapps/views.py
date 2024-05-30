from .services import ExchangeService
import asyncio
from celery import shared_task




async def update_exchange_data():
    service = ExchangeService()
    await service.fetch_and_save_currencies()
    await service.fetch_and_save_bitcoin_rate()

async def main():
    await update_exchange_data()

asyncio.run(main())




@shared_task
async def update_exchange_data():
    service = ExchangeService()
    await service.fetch_and_save_currencies()
    await service.fetch_and_save_bitcoin_rate()



