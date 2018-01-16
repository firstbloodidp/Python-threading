import time
import threadModule
import threading

threadModule.counter = 0

threadLock = threading.Lock()
threads = []
x = 42

for i in range(1,5):

   # Create new threads
   name = "Thread-"+ str(i)
   threads.append(threadModule.myThread(i, name, x))

   # Start new Threads
   threads[i-1].start()
   #time.sleep(1)

# Wait for all threads to complete
for t in threads:
   t.join()
print ("Exiting Main Thread")

print (threadModule.counter)