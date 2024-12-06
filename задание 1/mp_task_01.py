import threading
import time
import multiprocessing
import requests

# список url
urls = ['https://www.example.com'] * 10

def fetch_url(url):
    response = requests.get(url)
    return response.text

def sequence():
    start_time = time.perf_counter()  # время старта
    for url in urls:
        fetch_url(url)  # выполнение функции fetch_url для каждого url из urls
    end_time = time.perf_counter()  # время окончания
    print(f'sequence time: {end_time - start_time:0.2f} seconds\n')

def threads():
    start_time = time.perf_counter()  # время старта
    thread_list = []
    for url in urls:
        thread = threading.Thread(target=fetch_url, args=(url,))
        thread_list.append(thread)
        thread.start()

    for thread in thread_list:
        thread.join()  # ожидание окончания выполнения всех потоков
    end_time = time.perf_counter()  # время окончания
    print(f'threads time: {end_time - start_time:0.2f} seconds\n')

def processes():
    start_time = time.perf_counter()  # время старта
    with multiprocessing.Pool() as pool:
        pool.map(fetch_url, urls)  # выполнение с помощью процессов
    end_time = time.perf_counter()  # время окончания
    print(f'processes time: {end_time - start_time:0.2f} seconds\n')

if __name__ == '__main__':
    sequence()
    threads()
    processes()
