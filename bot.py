from telethon import TelegramClient, events

# --- ТВОИ ДАННЫЕ ---
API_ID = 33998764  
API_HASH = '000800f6aae8bb66f908fe8165626304'  
BOT_TOKEN = '9165019144:AAHUows6HMiDoukLazFN5OYH7OTVRQr4bM' 
ADMIN_ID = 8436425158  

# --- ТВОЙ НОВЫЙ ПРОКСИ ---
proxy_config = {
    'proxy_type': 'http',
    'addr': '4.144.146.21',
    'port': 80,
    'rdns': True
}

# Создаем клиента
client = TelegramClient('anon_bot', API_ID, API_HASH, proxy=proxy_config)

# --- ОБРАБОТКА СООБЩЕНИЙ ---
@client.on(events.NewMessage(incoming=True))
async def handler(event):
    if event.is_private:
        if event.sender_id == ADMIN_ID:
            await event.reply("Ты админ, сообщение не переслано.")
            return
        
        await client.send_message(ADMIN_ID, f"Новое анонимное сообщение:\n\n{event.text}")
        await event.reply("Твое сообщение отправлено анонимно!")

# --- ЗАПУСК ---
async def main():
    await client.start(bot_token=BOT_TOKEN)
    print("Бот запущен и работает!")
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())