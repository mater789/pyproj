import threading

class BoothThread(threading.Thread):
    def __init__(self, tid, monitor):
        self.tid          = tid
        self.monitor = monitor
        threading.Thread.__init__(self)
    def run(self):
        while True:
            monitor['lock'].acquire()                          # Lock; or wait if other thread is holding the lock
            if monitor['tick'] != 0:
                monitor['tick'] = monitor['tick'] - 1          # Sell tickets
                print(self.tid,':now left:',monitor['tick'])   # Tickets left
            else:
                print("Thread_id",self.tid," No more tickets")
                monitor['lock'].release()  # Unblock
                return                               # Exit the whole process immediately
            monitor['lock'].release()                          # Unblock

# Start of the main function
monitor = {'tick':30, 'lock':threading.Lock()}
# Start 10 threads
for k in range(10):
    new_thread = BoothThread(k, monitor)
    new_thread.start()