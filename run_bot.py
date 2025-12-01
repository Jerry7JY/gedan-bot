import asyncio
import sys
import os

# Загружаем переменные окружения
from dotenv import load_dotenv
load_dotenv()

# Windows fix
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def main():
    # Импортируем основной модуль только после настройки event loop
    import Gedan_bot
    
    try:
        print("=" * 50)
        print("🤖 ЗАПУСК БОТА GEDAN")
        print("=" * 50)
        
        # Проверяем токен
        BOT_TOKEN = os.getenv("BOT_TOKEN")
        if not BOT_TOKEN:
            print("❌ BOT_TOKEN не найден в .env файле!")
            print("💡 Создайте файл .env с содержанием:")
            print("BOT_TOKEN=ваш_токен_бота")
            return
        
        # Запускаем основной скрипт
        await Gedan_bot.main()
        
    except KeyboardInterrupt:
        print("\n👋 Бот остановлен")
    except Exception as e:
        print(f"❌ Ошибка при запуске: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())