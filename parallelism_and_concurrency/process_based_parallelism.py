from time import sleep, time
from multiprocessing import Process

def read():
    print("Executing...")
    sleep(3)

processes = []
timeout = 5

# Start the processes
for i in range(5):
    process = Process(target=read)
    process.start()
    processes.append(process)

# Verify and terminate the process
current_time = time()
for process in processes:
    while process.is_alive():
        if time() - current_time > timeout:
            process.kill()
            print(f"Proceso {process.pid} terminado por exceder el tiempo límite")
            break
        sleep(0.1)  # Short pause

    process.join()
