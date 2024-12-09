import requests
import json
import os
from datetime import datetime

# URL API Valetudo
VALETUDO_URL = "http://192.168.1.184:8080"

# Путь для сохранения карт
SAVE_PATH = "/путь/для/сохранения/карт"


# Функция для получения карты
def get_map():
    url = f"{VALETUDO_URL}/api/map/latest"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Ошибка при получении карты: {response.status_code}")
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

    # Декодируем изображение из base64
    import base64
    image_data = base64.b64decode(map_image)

    # Создаем имя файла с текущей датой и временем
    filename = f"map_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    file_path = os.path.join(SAVE_PATH, filename)

    # Сохраняем изображение
    with open(file_path, "wb") as f:
        f.write(image_data)

    print(f"Карта сохранена: {file_path}")


# Основная функция
def main():
    # Получаем карту
    map_data = get_map()

    # Сохраняем карту в формате PNG
    save_map_as_png(map_data)


if __name__ == "__main__":
    main()