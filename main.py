# import aiohttp
# import asyncio
#
# # Асинхронная функция для выполнения HTTP-запроса и получения данных
# async def get_data(url):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             return await response.text()
#
# # Основная асинхронная функция, выполняющая запросы одновременно
# async def main():
#     url1 = 'http://example.com/data1'
#     url2 = 'http://example.com/data2'
#     url3 = 'http://example.com/data3'
#
#     # Создаем задачи для выполнения запросов
#     task1 = asyncio.create_task(get_data(url1))
#     task2 = asyncio.create_task(get_data(url2))
#     task3 = asyncio.create_task(get_data(url3))
#
#     # Ожидаем завершения всех задач
#     data1 = await task1
#     data2 = await task2
#     data3 = await task3
#
#     # Выводим полученные данные
#     print(data1)
#     print(data2)
#     print(data3)
#
# # Запускаем основную функцию
# asyncio.run(main())
#
#
#
# import aiohttp
# import asyncio
#
# # Асинхронная функция для выполнения HTTP-запроса и получения данных
# async def fetch_data(session, url):
#     try:
#         async with session.get(url) as response:
#             response.raise_for_status()  # Проверка статуса ответа
#             return await response.json()  # Предполагаем, что сервер отдаёт JSON с числами
#     except aiohttp.ClientError as e:
#         print(f"Ошибка при загрузке данных с {url}: {e}")
#         return None
#
# # Асинхронная функция для обработки данных
# async def process_data():
#     async with aiohttp.ClientSession() as session:
#         urls = [
#             'http://example.com/data1',
#             'http://example.com/data2',
#             'http://example.com/data3'
#         ]
#
#         tasks = [fetch_data(session, url) for url in urls]
#         responses = await asyncio.gather(*tasks)
#
#         numbers = []
#         for response in responses:
#             if response is not None and 'number' in response:
#                 numbers.append(response['number'])
#
#         if numbers:
#             total_sum = sum(numbers)
#             average = total_sum / len(numbers)
#             print(f"Сумма чисел: {total_sum}")
#             print(f"Среднее значение: {average:.2f}")
#         else:
#             print("Не удалось получить данные для вычислений.")
#
# # Запуск асинхронной функции
# asyncio.run(process_data())
#
#
#
#
# import asyncio
#
# async def download_file(url):
#     print(f"Началась загрузка файла с {url}")
#     await asyncio.sleep(3)  # Имитация задержки сети
#     print(f"Файл с {url} загружен")
#
# async def main():
#     await download_file("http://example.com/file")
#
# asyncio.run(main())
#
#
#
#
# import asyncio
#
# # Асинхронная функция для имитации загрузки файла
# async def download_file(url):
#     print(f"Началась загрузка файла с {url}")
#     await asyncio.sleep(3)  # Имитация задержки сети
#     print(f"Файл с {url} загружен")
#
# # Основная функция
# async def main():
#     # Список URL для загрузки
#     urls = [
#         "http://example.com/file1",
#         "http://example.com/file2",
#         "http://example.com/file3"
#     ]
#
#     # Создаем задачи для параллельной загрузки файлов
#     tasks = [download_file(url) for url in urls]
#
#     # Используем asyncio.gather для выполнения всех задач параллельно
#     await asyncio.gather(*tasks)
#
# # Запуск основной функции
# asyncio.run(main())
#
#
#
#
#
# import asyncio
#
# # Асинхронная функция для имитации загрузки файла
# async def download_file(url):
#     try:
#         if "error" in url:
#             raise Exception("Ошибка загрузки")
#         print(f"Началась загрузка файла с {url}")
#         await asyncio.sleep(3)  # Имитация задержки сети
#         print(f"Файл с {url} загружен")
#     except Exception as e:
#         print(f"Ошибка при загрузке файла с {url}: {e}")
#
# # Основная функция
# async def main():
#     # Список URL для загрузки
#     urls = [
#         "http://example.com/file1",
#         "http://example.com/error_file",
#         "http://example.com/file2",
#         "http://example.com/file3",
#         "http://example.com/error_file2"
#     ]
#
#     # Создаем задачи для параллельной загрузки файлов
#     tasks = [download_file(url) for url in urls]
#
#     # Используем asyncio.gather для выполнения всех задач параллельно
#     await asyncio.gather(*tasks)
#
# # Запуск основной функции
# asyncio.run(main())
#
#
#
#
# import aiohttp
# import asyncio
# import time
#
# # Асинхронная функция для выполнения HTTP-запроса
# async def fetch_url(session, url):
#     async with session.get(url) as response:
#         return await response.text()
#
# # Асинхронная функция для выполнения всех запросов
# async def fetch_all(urls):
#     start_time = time.time()
#     async with aiohttp.ClientSession() as session:
#         tasks = [fetch_url(session, url) for url in urls]
#         results = await asyncio.gather(*tasks)
#     print(f"Длительность: {time.time() - start_time}")
#     return results
#
# # Основная функция для запуска асинхронного кода
# async def main():
#     urls = ["https://example.com", "https://example.org", "https://example.net"]
#     results = await fetch_all(urls)
#     for result in results:
#         print(result)
#
# # Запуск основной функции
# asyncio.run(main())
#
#
#
#
# import aiohttp
# import asyncio
# import time
#
# # Асинхронная функция для загрузки содержимого URL
# async def fetch_url(session, url):
#     async with session.get(url) as response:
#         return await response.text()
#
# # Асинхронная функция для загрузки нескольких URL и измерения времени
# async def fetch_multiple_urls(urls):
#     async with aiohttp.ClientSession() as session:
#         tasks = [fetch_url(session, url) for url in urls]
#         start_time = time.time()
#         results = await asyncio.gather(*tasks)
#         duration = time.time() - start_time
#     print(f"Общее время загрузки: {duration:.2f} секунд")
#     return results
#
# # Основная функция для запуска
# async def main():
#     urls = [
#         "https://example.com",
#         "https://example.org",
#         "https://example.net"
#     ]
#     results = await fetch_multiple_urls(urls)
#     for i, result in enumerate(results):
#         print(f"Содержимое {urls[i]}: {result[:100]}...")  # Выводим первые 100 символов содержимого
#
# # Запуск основной функции
# asyncio.run(main())
#
#
#
#
# import asyncio
#
# # Асинхронная подфункция с задержкой
# async def print_with_delay(value, delay):
#     await asyncio.sleep(delay)
#     print(f"Значение: {value} после задержки {delay} секунд")
#
# # Основная асинхронная функция, вызывающая две подфункции
# async def main():
#     # Создаем задачи для параллельного выполнения подфункций
#     task1 = print_with_delay("Первое значение", 2)
#     task2 = print_with_delay("Второе значение", 3)
#
#     # Параллельное выполнение задач
#     await asyncio.gather(task1, task2)
#
# # Запуск основной функции
# asyncio.run(main())
#
#
#
# import aiohttp
# import asyncio
# from urllib.parse import urlparse
#
# # Асинхронная функция для загрузки содержимого URL и сохранения в файл
# async def fetch_and_save_url(session, url):
#     try:
#         async with session.get(url) as response:
#             response.raise_for_status()  # Проверка статуса ответа
#             content = await response.text()
#             # Получаем имя хоста из URL
#             hostname = urlparse(url).hostname
#             if hostname:
#                 filename = f"{hostname}.txt"
#                 with open(filename, 'w', encoding='utf-8') as f:
#                     f.write(content)
#                 print(f"Сохранено содержимое из {url} в файл {filename}")
#             else:
#                 print(f"Не удалось определить имя хоста для URL: {url}")
#     except Exception as e:
#         print(f"Ошибка при загрузке данных с {url}: {e}")
#
# # Асинхронная функция для загрузки нескольких URL и измерения времени
# async def fetch_multiple_urls(urls):
#     async with aiohttp.ClientSession() as session:
#         tasks = [fetch_and_save_url(session, url) for url in urls]
#         start_time = time.time()
#         await asyncio.gather(*tasks)
#         duration = time.time() - start_time
#     print(f"Общее время загрузки: {duration:.2f} секунд")
#
# # Основная функция для запуска
# async def main():
#     urls = [
#         "https://example.com",
#         "https://example.org",
#         "https://example.net"
#     ]
#     await fetch_multiple_urls(urls)
#
# # Запуск основной функции
# asyncio.run(main())
#



import aiohttp
import asyncio
import time
from urllib.parse import urlparse

# Асинхронная функция для загрузки содержимого URL
async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

# Асинхронная функция для загрузки содержимого URL и сохранения в файл
async def fetch_and_save_url(session, url):
    try:
        async with session.get(url) as response:
            response.raise_for_status()  # Проверка статуса ответа
            content = await response.text()
            # Получаем имя хоста из URL
            hostname = urlparse(url).hostname
            if hostname:
                filename = f"{hostname}.txt"
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Сохранено содержимое из {url} в файл {filename}")
            else:
                print(f"Не удалось определить имя хоста для URL: {url}")
    except Exception as e:
        print(f"Ошибка при загрузке данных с {url}: {e}")

# Асинхронная подфункция с задержкой
async def print_with_delay(value, delay):
    await asyncio.sleep(delay)
    print(f"Значение: {value} после задержки {delay} секунд")

# Асинхронная функция для загрузки нескольких URL и измерения времени
async def fetch_multiple_urls(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_and_save_url(session, url) for url in urls]
        start_time = time.time()
        await asyncio.gather(*tasks)
        duration = time.time() - start_time
    print(f"Общее время загрузки: {duration:.2f} секунд")

# Основная функция для запуска всех задач
async def main():
    urls = [
        "https://example.com",
        "https://example.org",
        "https://example.net"
    ]

    # Задачи для загрузки и сохранения URL
    fetch_tasks = fetch_multiple_urls(urls)

    # Задачи для печати с задержкой
    print_task1 = print_with_delay("Первое значение", 2)
    print_task2 = print_with_delay("Второе значение", 3)

    # Запуск всех задач параллельно
    await asyncio.gather(fetch_tasks, print_task1, print_task2)

# Запуск основной функции
asyncio.run(main())






