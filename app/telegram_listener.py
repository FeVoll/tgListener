from pyrogram import Client, filters
from pybit.unified_trading import HTTP
import asyncio
import datetime


class TelegramListener:
    def __init__(self, api_id, api_hash, phone_number, whitelist):
        self.client = Client("my_account", api_id=api_id, api_hash=api_hash, phone_number=phone_number)
        self.whitelist = whitelist
        self.stop_event = asyncio.Event()  # Создаем Event для ожидания
        self.last_update_time = None  # Для отслеживания времени последнего сообщения

    async def start_listening(self):
        await self.client.start()

        # Получение доступных чатов
        dialogs = self.client.get_dialogs()
        print("Available channels and chats:")
        async for dialog in dialogs:
            print(f"Name: {dialog.chat.title}, ID: {dialog.chat.id}")

        # Основной цикл для проверки сообщений каждые 1 секунду
        while True:
            for chat_id in self.whitelist:
                try:
                    await self.fetch_latest_messages(chat_id, signal_parser, bybit_api)
                except TypeError:
                    print("error while parsing")
            await asyncio.sleep(1)  # Интервал в 1 секунду между проверками

    async def fetch_latest_messages(self, chat_id, signal_parser, bybit_api):
        # Получаем последние сообщения в чате
        async for message in self.client.get_chat_history(chat_id, limit=5):
            if self.last_update_time is None or message.date > self.last_update_time:
                self.last_update_time = message.date  # Обновляем время последнего сообщения
                print(message.text)

                #Ваша логика

    async def stop(self):
        # Остановка клиента и выставление флага завершения
        await self.client.stop()
        self.stop_event.set()  # Сообщаем о завершении работы
