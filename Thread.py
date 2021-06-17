import threading
import time
class sub(threading.Thread):
    def __init__(self,name,time):
        threading.Thread.__init__(self)
        self.name=name
        self.time=time
    def run(self):
        for i in range(self.time):
            time.sleep(3)
            print(self.name)
t1=sub("T1",3)
t2=sub("T2",10)
t1.start()
t2.start()
