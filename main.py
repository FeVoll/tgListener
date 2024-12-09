import asyncio
from app.telegram_listener import TelegramListener


async def main():

    api_id = "123312" # id
    api_hash = "12312312" #hash
    phone_number = "+123123" #номер
    whitelist = [-100123123, -100213123] #чаты

    telegram_listener = TelegramListener(api_id, api_hash, phone_number, whitelist)

    # Ожидание старта прослушивания Telegram-сообщений
    await telegram_listener.start_listening(signal_parser, bybit_api)

if __name__ == "__main__":
    # Запуск основного асинхронного цикла
    asyncio.run(main())
