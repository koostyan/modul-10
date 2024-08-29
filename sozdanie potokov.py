import threading
from time import sleep
from datetime import datetime

time_start = datetime.now()


def wite_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(1, word_count + 1):
            f.write(f"Какое-то слово № {i}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")


wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')

time_end = datetime.now()
print(f'Работа функции {time_end - time_start}')

time_start = datetime.now()

threads = []
threads.append(threading.Thread(target=wite_words, args=(10, 'example5.txt')))
threads.append(threading.Thread(target=wite_words, args=(30, 'example6.txt')))
threads.append(threading.Thread(target=wite_words, args=(200, 'example7.txt')))
threads.append(threading.Thread(target=wite_words, args=(100, 'example8.txt')))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
time_end = datetime.now()
time_res = time_end - time_start
print(f'Работа потоков {time_res}')
