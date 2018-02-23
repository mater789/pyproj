import threading
import time

class Producer(threading.Thread):
    stopped = False
    def run(self):
        global count
        while True:
            if con.acquire():
                if count > 1000:
                    con.wait()
                else:
                    count = count+100
                    msg = self.name+' produce 100, count='+ count.__str__()
                    print(msg)
                    con.notify()
                con.release()
                time.sleep(1)
            if self.stopped == True:
                break

    def stop(self):
        self.stopped = True

class Consumer(threading.Thread):
    stopped = False
    def run(self):
        global count
        while True:
            if con.acquire():
                if count < 100:
                    con.wait()
                else:
                    count = count-3
                    msg = self.name+' consume 3, count='+ count.__str__()
                    print(msg)
                    con.notify()
                con.release()
                time.sleep(1)
            if self.stopped == True:
                break

    def stop(self):
        self.stopped = True

count = 500
con = threading.Condition()
def test():
    t = []
    for i in range(2):
        p = Producer()
        p.start()
        t.append(p)
    for i in range(5):
        c = Consumer()
        c.start()
        t.append(c)
    for te in t:
        te.stop()

test()
