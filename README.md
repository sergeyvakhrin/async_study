# async_study

В этом разделе вы найдете задачи для самостоятельной практики. В спойлерах под каждой задачей скрыто решение и пояснения к этому решению. Обращайтесь к решению после того, как решили задачу самостоятельно или столкнулись с трудностями в решении.

Задача 1
Дан следующий синхронный код, который загружает текстовую информацию с трёх различных URL-адресов по порядку:

import requests

def get_data(url):
    response = requests.get(url)
    return response.text

data1 = get_data('<http://example.com/data1>')
data2 = get_data('<http://example.com/data2>')
data3 = get_data('<http://example.com/data3>')

print(data1)
print(data2)
print(data3)
Перепишите данный код, используя асинхронный подход с 
asyncio
 и 
aiohttp
, чтобы запросы отправлялись одновременно.


Решение

Задача 2
Рассмотрим сценарий, где после получения данных необходимо их асинхронно обработать. Например, предположим, что данные содержат цифры, и вам нужно вычислить их сумму после извлечения.

import aiohttp
import asyncio

async def fetch_data(session, url):
    async with session.get(url) as response:
        return await response.json()  # предполагаем, что сервер отдаёт JSON с числами

async def process_data():
    async with aiohttp.ClientSession() as session:
        data1 = await fetch_data(session, '<http://example.com/data1>')
        data2 = await fetch_data(session, '<http://example.com/data2>')
        data3 = await fetch_data(session, '<http://example.com/data3>')

        # Предположим, что каждый response.json() возвращает {'number': число}
        result = data1['number'] + data2['number'] + data3['number']
        print(f"Сумма чисел: {result}")

# Запуск асинхронной функции
asyncio.run(process_data())
Добавьте обработку ошибок для каждого запроса. В случае ошибки при загрузке данных из URL, должно выводиться сообщение об ошибке и число должно в сумму не включаться.

Рассчитайте среднее значение суммированных чисел.


Решение
import aiohttp
import asyncio

# Асинхронная функция для выполнения HTTP-запроса и получения данных
async def fetch_data(session, url):
    try:
        async with session.get(url) as response:
            response.raise_for_status()  # Проверка статуса ответа
            return await response.json()  # Предполагаем, что сервер отдаёт JSON с числами
    except aiohttp.ClientError as e:
        print(f"Ошибка при загрузке данных с {url}: {e}")
        return None

# Асинхронная функция для обработки данных
async def process_data():
    async with aiohttp.ClientSession() as session:
        urls = [
            'http://example.com/data1',
            'http://example.com/data2',
            'http://example.com/data3'
        ]

        tasks = [fetch_data(session, url) for url in urls]
        responses = await asyncio.gather(*tasks)

        numbers = []
        for response in responses:
            if response is not None and 'number' in response:
                numbers.append(response['number'])

        if numbers:
            total_sum = sum(numbers)
            average = total_sum / len(numbers)
            print(f"Сумма чисел: {total_sum}")
            print(f"Среднее значение: {average:.2f}")
        else:
            print("Не удалось получить данные для вычислений.")

# Запуск асинхронной функции
asyncio.run(process_data())
Объяснение:
Импорт модулей:
import aiohttp
import asyncio
Импортируем необходимые модули для асинхронных HTTP-запросов и управления асинхронными задачами.

Асинхронная функция 
fetch_data
:
async def fetch_data(session, url):
    try:
        async with session.get(url) as response:
            response.raise_for_status()  # Проверка статуса ответа
            return await response.json()  # Предполагаем, что сервер отдаёт JSON с числами
    except aiohttp.ClientError as e:
        print(f"Ошибка при загрузке данных с {url}: {e}")
        return None
Выполняем HTTP-запрос к указанному URL.
Проверяем статус ответа с помощью 
raise_for_status()
. Если статус не успешный, генерируется исключение.
В случае ошибки при запросе, выводим сообщение об ошибке и возвращаем 
None
.
Асинхронная функция 
process_data
:
async def process_data():
    async with aiohttp.ClientSession() as session:
        urls = [
            'http://example.com/data1',
            'http://example.com/data2',
            'http://example.com/data3'
        ]

        tasks = [fetch_data(session, url) for url in urls]
        responses = await asyncio.gather(*tasks)

        numbers = []
        for response in responses:
            if response is not None and 'number' in response:
                numbers.append(response['number'])

        if numbers:
            total_sum = sum(numbers)
            average = total_sum / len(numbers)
            print(f"Сумма чисел: {total_sum}")
            print(f"Среднее значение: {average:.2f}")
        else:
            print("Не удалось получить данные для вычислений.")
Создаем сессию и список URL-адресов.
Создаем задачи для выполнения запросов с помощью 
fetch_data
 и собираем их в список 
tasks
.
Используем 
asyncio.gather
 для выполнения всех задач одновременно.
Проверяем ответы, собирая числа в список 
numbers
.
Если удалось получить данные, рассчитываем и выводим сумму и среднее значение.
Если не удалось получить данные, выводим соответствующее сообщение.
Запуск асинхронной функции:
asyncio.run(process_data())
Используем 
asyncio.run()
 для запуска основной асинхронной функции 
process_data
.


Задание 3
Напишите асинхронную функцию 
download_file
, которая имитирует загрузку файла из сети. Пусть функция принимает параметр 
url
 и использует 
await asyncio.sleep(3)
, чтобы имитировать временную задержку сетевой операции.
В функции 
main
, вызовите вашу функцию 
download_file
 с любым URL в виде строки.
Используйте 
asyncio.run()
 для запуска функции 
main
 и проверьте работоспособность вашего кода.

Решение
import asyncio

async def download_file(url):
    print(f"Началась загрузка файла с {url}")
    await asyncio.sleep(3)  # Имитация задержки сети
    print(f"Файл с {url} загружен")

async def main():
    await download_file("http://example.com/file")

asyncio.run(main())
Объяснение:
Импортируем модуль 
asyncio
:
import asyncio
Мы импортируем модуль 
asyncio
, который предоставляет возможности для асинхронного программирования.

Определение асинхронной функции 
download_file
:
pythonКопировать код
async def download_file(url):
    print(f"Началась загрузка файла с {url}")
    await asyncio.sleep(3)  # Имитация задержки сети
    print(f"Файл с {url} загружен")
Ключевое слово 
async
 перед 
def
 указывает, что функция является асинхронной.
Внутри функции мы используем 
await asyncio.sleep(3)
 для имитации временной задержки сетевой операции.
Определение основной асинхронной функции 
main
:
async def main():
    await download_file("http://example.com/file")
В этой функции мы вызываем 
download_file
 с указанным URL и ждем завершения выполнения функции с помощью 
await
.

Запуск основной функции с использованием 
asyncio.run()
:
asyncio.run(main())
asyncio.run(main())
 запускает выполнение асинхронной функции 
main
 и управляет циклом событий для выполнения всех задач.

Задание 4
Используя функцию 
download_file
 из предыдущего задания, модифицируйте функцию 
main
, чтобы одновременно загружать три файла с разных URL.
Для этого используйте 
asyncio.gather()
 для параллельной загрузки файлов.
Проверьте, что все файлы начинают загружаться практически одновременно и что общее время выполнения программы сократилось по сравнению с последовательной загрузкой.

Решение
import asyncio

# Асинхронная функция для имитации загрузки файла
async def download_file(url):
    print(f"Началась загрузка файла с {url}")
    await asyncio.sleep(3)  # Имитация задержки сети
    print(f"Файл с {url} загружен")

# Основная функция
async def main():
    # Список URL для загрузки
    urls = [
        "http://example.com/file1",
        "http://example.com/file2",
        "http://example.com/file3"
    ]

    # Создаем задачи для параллельной загрузки файлов
    tasks = [download_file(url) for url in urls]

    # Используем asyncio.gather для выполнения всех задач параллельно
    await asyncio.gather(*tasks)

# Запуск основной функции
asyncio.run(main())
Объяснение:
Импортируем модуль 
asyncio
:
import asyncio
Мы импортируем модуль 
asyncio
, который предоставляет возможности для асинхронного программирования.

Определение асинхронной функции 
download_file
:
async def download_file(url):
    print(f"Началась загрузка файла с {url}")
    await asyncio.sleep(3)  # Имитация задержки сети
    print(f"Файл с {url} загружен")
Функция 
download_file
 имитирует загрузку файла, используя 
await asyncio.sleep(3)
 для создания временной задержки.
Определение основной асинхронной функции 
main
:
async def main():
    # Список URL для загрузки
    urls = [
        "http://example.com/file1",
        "http://example.com/file2",
        "http://example.com/file3"
    ]

    # Создаем задачи для параллельной загрузки файлов
    tasks = [download_file(url) for url in urls]

    # Используем asyncio.gather для выполнения всех задач параллельно
    await asyncio.gather(*tasks)
Внутри 
main
 создаем список URL, которые мы хотим загрузить.
Используем список 
tasks
, который содержит задачи для загрузки каждого файла.
Используем 
asyncio.gather
 для параллельного выполнения всех задач.
Запуск основной функции с использованием 
asyncio.run()
:
asyncio.run(main())
asyncio.run(main())
 запускает выполнение асинхронной функции 
main
 и управляет циклом событий для выполнения всех задач.

Задание 5
Добавьте в функцию 
download_file
 генерацию исключения на определённых URL. Например, если URL содержит "error", функция должна возбуждать исключение 
Exception("Ошибка загрузки")
.
В функции 
main
, попробуйте загрузить несколько файлов, некоторые из которых должны привести к исключениям.
Используйте конструкцию 
try...except
, чтобы обрабатывать исключения, и убедитесь, что ваша программа корректно сообщает об ошибках, не прерывая загрузку остальных файлов.

Решение
import asyncio

# Асинхронная функция для имитации загрузки файла
async def download_file(url):
    try:
        if "error" in url:
            raise Exception("Ошибка загрузки")
        print(f"Началась загрузка файла с {url}")
        await asyncio.sleep(3)  # Имитация задержки сети
        print(f"Файл с {url} загружен")
    except Exception as e:
        print(f"Ошибка при загрузке файла с {url}: {e}")

# Основная функция
async def main():
    # Список URL для загрузки
    urls = [
        "http://example.com/file1",
        "http://example.com/error_file",
        "http://example.com/file2",
        "http://example.com/file3",
        "http://example.com/error_file2"
    ]

    # Создаем задачи для параллельной загрузки файлов
    tasks = [download_file(url) for url in urls]

    # Используем asyncio.gather для выполнения всех задач параллельно
    await asyncio.gather(*tasks)

# Запуск основной функции
asyncio.run(main())
Объяснение:
Импортируем модуль 
asyncio
:
import asyncio
Мы импортируем модуль 
asyncio
, который предоставляет возможности для асинхронного программирования.

Модификация функции 
download_file
:
async def download_file(url):
    try:
        if "error" in url:
            raise Exception("Ошибка загрузки")
        print(f"Началась загрузка файла с {url}")
        await asyncio.sleep(3)  # Имитация задержки сети
        print(f"Файл с {url} загружен")
    except Exception as e:
        print(f"Ошибка при загрузке файла с {url}: {e}")
Добавляем проверку 
if "error" in url
 для генерации исключения.
Используем блок 
try...except
 для обработки исключений.
Если возникает исключение, оно обрабатывается и выводится сообщение об ошибке, не прерывая выполнение остальных задач.
Определение основной асинхронной функции 
main
:
async def main():
    # Список URL для загрузки
    urls = [
        "http://example.com/file1",
        "http://example.com/error_file",
        "http://example.com/file2",
        "http://example.com/file3",
        "http://example.com/error_file2"
    ]

    # Создаем задачи для параллельной загрузки файлов
    tasks = [download_file(url) for url in urls]

    # Используем asyncio.gather для выполнения всех задач параллельно
    await asyncio.gather(*tasks)
Создаем список URL для загрузки, включая некоторые URL, которые приведут к исключениям.
Создаем задачи для каждой загрузки файла.
Используем 
asyncio.gather
 для параллельного выполнения всех задач.
Запуск основной функции с использованием 
asyncio.run()
:
asyncio.run(main())
asyncio.run(main())
 запускает выполнение асинхронной функции 
main
 и управляет циклом событий для выполнения всех задач.

Задание 6
Преобразуйте данный синхронный код в асинхронный.

import requests
import time

def fetch_url(url):
    response = requests.get(url)
    return response.text

def fetch_all(urls):
    start_time = time.time()
    results = []
    for url in urls:
        result = fetch_url(url)
        results.append(result)
    print(f"Длительность: {time.time() - start_time}")
    return results

urls = ["<https://example.com>", "<https://example.org>", "<https://example.net>"]
fetch_all(urls)

Решение
import aiohttp
import asyncio
import time

# Асинхронная функция для выполнения HTTP-запроса
async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

# Асинхронная функция для выполнения всех запросов
async def fetch_all(urls):
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
    print(f"Длительность: {time.time() - start_time}")
    return results

# Основная функция для запуска асинхронного кода
async def main():
    urls = ["https://example.com", "https://example.org", "https://example.net"]
    results = await fetch_all(urls)
    for result in results:
        print(result)

# Запуск основной функции
asyncio.run(main())
Объяснение:
Импортируем модули:
import aiohttp
import asyncio
import time
Импортируем необходимые модули для асинхронных HTTP-запросов и управления асинхронными задачами.

Определение асинхронной функции 
fetch_url
:
async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()
Функция 
fetch_url
 принимает сессию и URL.
Выполняет асинхронный GET-запрос и возвращает текст ответа.
Определение асинхронной функции 
fetch_all
:
async def fetch_all(urls):
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
    print(f"Длительность: {time.time() - start_time}")
    return results
Создаем сессию для выполнения HTTP-запросов.
Создаем задачи для каждого URL и собираем их в список 
tasks
 .
Используем 
asyncio.gather
 для параллельного выполнения всех задач.
Измеряем и выводим время выполнения.
Определение основной функции 
main
:
async def main():
    urls = ["https://example.com", "https://example.org", "https://example.net"]
    results = await fetch_all(urls)
    for result in results:
        print(result)
Основная функция, которая определяет список URL и вызывает функцию 
fetch_all
.
Выводит результаты каждого запроса.
Запуск основной функции с использованием 
asyncio.run()
:
asyncio.run(main())
asyncio.run(main())
 запускает выполнение асинхронной функции 
main
 и управляет циклом событий для выполнения всех задач.

Задание 7
Напишите асинхронную функцию 
fetch_url
, которая с использованием библиотеки 
aiohttp
 будет загружать содержимое URL и возвращать его. Создайте еще одну функцию, которая будет использовать 
fetch_url
 для асинхронной загрузки трех разных URL и измеряйте общее время загрузки. Удостоверьтесь, что код делает асинхронные вызовы.


Решение
import aiohttp
import asyncio
import time

# Асинхронная функция для загрузки содержимого URL
async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

# Асинхронная функция для загрузки нескольких URL и измерения времени
async def fetch_multiple_urls(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        start_time = time.time()
        results = await asyncio.gather(*tasks)
        duration = time.time() - start_time
    print(f"Общее время загрузки: {duration:.2f} секунд")
    return results

# Основная функция для запуска
async def main():
    urls = [
        "https://example.com",
        "https://example.org",
        "https://example.net"
    ]
    results = await fetch_multiple_urls(urls)
    for i, result in enumerate(results):
        print(f"Содержимое {urls[i]}: {result[:100]}...")  # Выводим первые 100 символов содержимого

# Запуск основной функции
asyncio.run(main())
Объяснение:
Импортируем модули:
import aiohttp
import asyncio
import time
Импортируем необходимые модули для асинхронных HTTP-запросов и управления асинхронными задачами.

Определение асинхронной функции 
fetch_url
:
async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()
Функция 
fetch_url
 принимает сессию и URL.
Выполняет асинхронный GET-запрос и возвращает текст ответа.
Определение асинхронной функции 
fetch_multiple_urls
:
async def fetch_multiple_urls(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        start_time = time.time()
        results = await asyncio.gather(*tasks)
        duration = time.time() - start_time
    print(f"Общее время загрузки: {duration:.2f} секунд")
    return results
Создаем сессию для выполнения HTTP-запросов.
Создаем задачи для каждого URL и собираем их в список 
tasks
.
Запускаем параллельное выполнение всех задач с 
asyncio.gather
.
Измеряем и выводим общее время загрузки.
Определение основной функции 
main
:
async def main():
    urls = [
        "https://example.com",
        "https://example.org",
        "https://example.net"
    ]
    results = await fetch_multiple_urls(urls)
    for i, result in enumerate(results):
        print(f"Содержимое {urls[i]}: {result[:100]}...")  # Выводим первые 100 символов содержимого
Основная функция, которая определяет список URL и вызывает функцию 
fetch_multiple_urls
.
Выводит результаты каждого запроса, показывая первые 100 символов содержимого.
Запуск основной функции с использованием 
asyncio.run()
:
asyncio.run(main())
asyncio.run(main())
 запускает выполнение асинхронной функции 
main
 и управляет циклом событий для выполнения всех задач.

Задание 8
Создайте следующую асинхронную задачу с использованием 
asyncio
. Напишите функцию, вызывающую две асинхронные подфункции, где каждая будет с некоторой задержкой (используйте 
asyncio.sleep
) печатать переданное ей на вход значение. Создайте цикл событий и убедитесь, что обе функции работают параллельно.


Решение
import asyncio

# Асинхронная подфункция с задержкой
async def print_with_delay(value, delay):
    await asyncio.sleep(delay)
    print(f"Значение: {value} после задержки {delay} секунд")

# Основная асинхронная функция, вызывающая две подфункции
async def main():
    # Создаем задачи для параллельного выполнения подфункций
    task1 = print_with_delay("Первое значение", 2)
    task2 = print_with_delay("Второе значение", 3)

    # Параллельное выполнение задач
    await asyncio.gather(task1, task2)

# Запуск основной функции
asyncio.run(main())
Объяснение:
Импортируем модуль 
asyncio
:
import asyncio
Мы импортируем модуль 
asyncio
, который предоставляет возможности для асинхронного программирования.

Определение асинхронной подфункции 
print_with_delay
:
async def print_with_delay(value, delay):
    await asyncio.sleep(delay)
    print(f"Значение: {value} после задержки {delay} секунд")
Функция принимает два параметра: 
value
 (значение для печати) и 
delay
 (время задержки в секундах).
Использует 
await asyncio.sleep(delay)
 для создания задержки.
Печатает переданное значение после указанной задержки.
Определение основной функции 
main
:
async def main():
    # Создаем задачи для параллельного выполнения подфункций
    task1 = print_with_delay("Первое значение", 2)
    task2 = print_with_delay("Второе значение", 3)

    # Параллельное выполнение задач
    await asyncio.gather(task1, task2)
В основной функции создаем задачи для выполнения подфункций 
print_with_delay
 с разными значениями и задержками.
Используем 
asyncio.gather
 для параллельного выполнения задач.
Запуск основной функции с использованием 
asyncio.run()
:
asyncio.run(main())
asyncio.run(main())
 запускает выполнение асинхронной функции 
main
 и управляет циклом событий для выполнения всех задач.

Задание 9
Дополните асинхронную функцию из задания 7, так чтобы она не только загружала данные по URL, но и сохраняла полученный результат в файл. Название файла должно соответствовать имени хоста URL. Проверьте работоспособность вашего кода, загрузив несколько файлов асинхронно.


Решение
import aiohttp
import asyncio
from urllib.parse import urlparse

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

# Асинхронная функция для загрузки нескольких URL и измерения времени
async def fetch_multiple_urls(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_and_save_url(session, url) for url in urls]
        start_time = time.time()
        await asyncio.gather(*tasks)
        duration = time.time() - start_time
    print(f"Общее время загрузки: {duration:.2f} секунд")

# Основная функция для запуска
async def main():
    urls = [
        "https://example.com",
        "https://example.org",
        "https://example.net"
    ]
    await fetch_multiple_urls(urls)

# Запуск основной функции
asyncio.run(main())
Объяснение:
Импортируем модули:
import aiohttp
import asyncio
import os
from urllib.parse import urlparse
Импортируем необходимые модули для асинхронных HTTP-запросов, управления асинхронными задачами, работы с файловой системой и парсинга URL.

Определение асинхронной функции 
fetch_and_save_url
:
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
Функция принимает сессию и URL.
Выполняет асинхронный GET-запрос и проверяет статус ответа.
Получает текст ответа.
Определяет имя хоста из URL и сохраняет содержимое в файл с именем хоста.
Обрабатывает исключения и выводит сообщения об ошибках.
Определение асинхронной функции 
fetch_multiple_urls
:
async def fetch_multiple_urls(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_and_save_url(session, url) for url in urls]
        start_time = time.time()
        await asyncio.gather(*tasks)
        duration = time.time() - start_time
    print(f"Общее время загрузки: {duration:.2f} секунд")
Создаем сессию для выполнения HTTP-запросов.
Создаем задачи для каждого URL и собираем их в список 
tasks
.
Запускаем параллельное выполнение всех задач с 
asyncio.gather
.
Измеряем и выводим общее время загрузки.
Определение основной функции 
main
:
async def main():
    urls = [
        "https://example.com",
        "https://example.org",
        "https://example.net"
    ]
    await fetch_multiple_urls(urls)
Основная функция, которая определяет список URL и вызывает функцию 
fetch_multiple_urls
.
Запуск основной функции с использованием 
asyncio.run()
:
asyncio.run(main())
asyncio.run(main())
 запускает выполнение асинхронной функции 
main
 и управляет циклом событий для выполнения всех задач.

Задание 10
Объедините все асинхронные функции, созданные в заданиях 6-9, в один скрипт. Запустите их в одной асинхронной сессии и убедитесь, что все функции выполняются корректно и эффективно используют асинхронность для повышения производительности программы.


Решение
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
Объяснение:
Импортируем модули:
import aiohttp
import asyncio
import time
from urllib.parse import urlparse
Импортируем необходимые модули для асинхронных HTTP-запросов, управления асинхронными задачами, измерения времени и парсинга URL.

Определение асинхронной функции 
fetch_url
:
async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()
Эта функция загружает содержимое URL и возвращает его.
Определение асинхронной функции 
fetch_and_save_url
:
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
Эта функция загружает содержимое URL и сохраняет его в файл, имя которого соответствует имени хоста URL.
Определение асинхронной подфункции 
print_with_delay
:
async def print_with_delay(value, delay):
    await asyncio.sleep(delay)
    print(f"Значение: {value} после задержки {delay} секунд")
Эта функция с задержкой (используя 
asyncio.sleep
) печатает переданное значение.
Определение основной функции 
main
:
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
Основная функция, которая запускает все асинхронные задачи параллельно.
Запуск основной функции с использованием 
asyncio.run()
:
asyncio.run(main())
asyncio.run(main())
 запускает выполнение асинхронной функции 
main
 и управляет циклом событий для выполнения всех задач.