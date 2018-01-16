import threading
import time

class myThread(threading.Thread):
   def __init__(self, threadID, name, x):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.light = 0
      self.maxCounter = x

   def run(self):
      print ("Starting " + self.name)
      # Get lock to synchronize threads
      # threadLock.acquire() 
      global counter
      while counter < self.maxCounter:
         if counter < self.maxCounter and self.light == 0 :
            self.light = 1
            counter += 1
            #print (self.name,counter)
            #time.sleep(4) 
            self.light = 0
      # Free lock to release next thread
      # threadLock.release()
