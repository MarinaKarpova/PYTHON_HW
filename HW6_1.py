import time
class Trafficlight:
   __colors=['red', 'yellow', 'green']
   def __init__(self):
       pass
   def running(self):
       while True:
           print('red')
           time.sleep(7)
           print('yellow')
           time.sleep(2)
           print('green')
           time.sleep(7)
a=Trafficlight()
a.running()