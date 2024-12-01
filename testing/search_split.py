import os
import threading
import time

stop_search = False
lock = threading.Lock()

def find_line_by_full_name(file_path, full_name, stop: bool):
    global stop_search
    with open(file_path, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, start=1):
            if stop_search and stop:
                return 
            if full_name.lower() in line.lower():
                with lock:
                    if not stop_search or not stop:
                        stop_search = True
                        print(f'Найдена строка {line_number}: {line.strip()} в файле {file_path}')
                return 

def search(search_full_name, stop: bool):
    global stop_search
    threads = []
    
    for filename in os.listdir(".\\output"):
        if not os.path.isdir(filename):
            for filename_dir in os.listdir(f".\\output\\{filename}"): 
                if stop_search and stop:
                    break
                file_path = f".\\output\\{filename}\\{filename_dir}"
                thread = threading.Thread(target=find_line_by_full_name, args=(file_path, search_full_name, stop))
                threads.append(thread)
                thread.start()
        else:
            file_path = filename  
            thread = threading.Thread(target=find_line_by_full_name, args=(f".\\output\\{file_path}", search_full_name))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()

start_time = time.time()
search("нигматуллин арсен фаилевич", stop=True)
end_time = time.time()
if not stop_search:
    print(f"Не найдено. Время поиска: {end_time - start_time:.2f} секунд")
else:
    print(f"Время поиска: {end_time - start_time:.2f}")