import threading
import time

def doChore():
    time.sleep(0.5)

def booth(tid):
    global i
    global lock
    while True:
        lock.acquire()                # Lock; or wait if other thread is holding the lock
        if i != 0:
            i = i - 1                 # Sell tickets
            print(tid,':now left:',i) # Tickets left
            #doChore()                 # Other critical operations
        else:
            print("Thread_id",tid," No more tickets")
            lock.release()  # Unblock
            return None              # Exit the whole process immediately
        lock.release()  # Unblock
        #doChore()                    # Non-critical operations

i = 30                           # Available ticket number
lock = threading.Lock()              # Lock (i.e., mutex)
thr = []
for k in range(10):
    new_thread = threading.Thread(target=booth,args=(k,))   # Set up thread; target: the callable (function) to be run, args: the argument for the callable
    new_thread.start()                                      # run the thread
    thr.append(new_thread)
for t in thr:
    t.join()