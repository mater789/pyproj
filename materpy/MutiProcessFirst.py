import multiprocessing
import os

def worker(sign, lock):
    lock.acquire()
    print(sign, os.getpid())
    lock.release()

#必须放if __name__ == '__main__':
if __name__ == '__main__':
    print('Main:', os.getpid())
    multiprocessing.freeze_support()
    record = []
    lock = multiprocessing.Lock()
    for i in range(5):
        process = multiprocessing.Process(target=worker,args=('process',lock))
        process.start()
        record.append(process)
    for process in record:
        process.join()
