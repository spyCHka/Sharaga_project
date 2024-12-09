import requests
import json
import os
from datetime import datetime
import base64
import urllib3

# Отключаем предупреждение
urllib3.disable_warnings(urllib3.exceptions.NotOpenSSLWarning)

# URL API Valetudo
VALETUDO_URL = "http://<ваш_ip_робота>:8080"

# Путь для сохранения карт
SAVE_PATH = "/путь/для/сохранения/карт"


# Функция для получения карты
def get_map():
    url = f"{VALETUDO_URL}/api/map/latest"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка на ошибки HTTP
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при получении карты: {e}")
        return None


# Функция для сохранения карты в формате PNG
def save_map_as_png(map_data):
    if not map_data:
        print("Нет данных карты для сохранения.")
        return

    # Извлекаем данные карты
    map_image = map_data.get("map", {}).get("image")
    if not map_image:
        print("Карта не содержит изображения.")
        return

    try:
        # Декодируем изображение из base64
        image_data = base64.b64decode(map_image)
    except Exception as e:
        print(f"Ошибка при декодировании изображения: {e}")
        return

    # Создаем имя файла с текущей датой и временем
    filename = f"map_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    file_path = os.path.join(SAVE_PATH, filename)

    try:
        # Сохраняем изображение
        with open(file_path, "wb") as f:
            f.write(image_data)
        print(f"Карта сохранена: {file_path}")
    except Exception as e:
        print(f"Ошибка при записи файла: {e}")


# Основная функция
def main():
    # Получаем карту
    map_data = get_map()

    # Сохраняем карту в формате PNG
    save_map_as_png(map_data)


if __name__ == "__main__":
    main()