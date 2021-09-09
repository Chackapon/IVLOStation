import time
import ivlos
from turtle_stuff import *
def startup():
  time.sleep(1)
  
  launch_title.write("IVLOStation", move=False, align="center", font=("Arial", int(screen.screensize()[0]/10), "normal"))
  launch_title.sety(-30)
  launch_title.write("feel your inner gamer", move=False, align="center", font=("Arial", int(screen.screensize()[0]/30), "normal"))
  print("Complete")
  launch_title.ht()
  time.sleep(10)
  
  ivlos.menu()