import logging
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Вставьте свой API-ключ OpenWeatherMap
API_KEY = "baa12bb7d2ed31c6c4b31e8a5d40d726"
# Токен Telegram-бота
BOT_TOKEN = "7547624413:AAH5QWnNL4MsYJBApfq_ahpc-zlL-OMxzZw"

# Функция получения погоды для города
def get_weather(city: str, days: int = 1):
    # Если запрашиваем погоду на 1 день, используем текущую погоду
    if days == 1:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ru"
    # Для прогноза на 3 дня
    elif days == 3:
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric&lang=ru"
    else:
        return "Данные о погоде не поддерживаются для этого количества дней."

    response = requests.get(url)
    data = response.json()

    # Если получен правильный ответ
    if data.get("cod") == "404":
        return f"Город {city} не найден!"
    
    # Если запрашиваем текущую погоду
    if days == 1:
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        return f"Погода в городе {city}:\nТемпература: {temp}°C\nОписание: {description}\nВлажность: {humidity}%\nСкорость ветра: {wind_speed} м/с"
    
    # Для прогноза на 3 дня
    elif days == 3:
        forecast = ""
        day_counter = 1
        for entry in data["list"]:
            # Мы получаем прогнозы через каждые 3 часа, поэтому соберем прогнозы только для 3 дней
            # Каждый день имеет 8 записей (по 3 часа)
            if entry["dt_txt"].endswith("00:00:00"):
                dt_txt = entry["dt_txt"]
                temp = entry["main"]["temp"]
                description = entry["weather"][0]["description"]
                forecast += f"\n\nДень {day_counter} ({dt_txt}): {temp}°C, {description}"
                day_counter += 1
            if day_counter > 3:  # Мы должны ограничиться 3 днями
                break
        return f"Прогноз погоды в городе {city} на 3 дня:{forecast}"

# Функция для команды /weather
async def weather(update: Update, context: CallbackContext):
    if len(context.args) == 0:
        await update.message.reply_text("Пожалуйста, укажите город после команды, например: /weather Москва")
        return
    
    city = " ".join(context.args)
    
    # Получаем текущую погоду
    weather_info = get_weather(city, days=1)
    await update.message.reply_text(weather_info)

# Функция для команды /forecast
async def forecast(update: Update, context: CallbackContext):
    if len(context.args) == 0:
        await update.message.reply_text("Пожалуйста, укажите город после команды, например: /forecast Москва")
        return
    
    city = " ".join(context.args)
    
    # Получаем прогноз на 3 дня
    forecast_info = get_weather(city, days=3)
    await update.message.reply_text(forecast_info)

# Функция для старта
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "Привет! Я могу предоставить погоду за один день и прогноз на три дня. Используй команды:\n"
        "/weather <город> — для текущей погоды\n"
        "/forecast <город> — для прогноза на три дня"
    )

def main():
    # Включаем логирование для отладки
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Создаем объект приложения (для версии 20+)
    application = Application.builder().token(BOT_TOKEN).build()

    # Регистрируем обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("weather", weather))
    application.add_handler(CommandHandler("forecast", forecast))

    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()
