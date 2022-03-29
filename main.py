import os
from time import sleep
import JARVIS
from JARVIS import *
from JARVIS import intelligence
import sys 
import time 
import threading


#Instalizing the interface gif
def interface():
    sleep(3)
    os.system('cmd/c"Customisation\Rainmeter"')



#Multiprocessing with interface
the_process = threading.Thread(name='process',target=interface)
the_process.start()

while the_process.is_alive():
    intelligence()


