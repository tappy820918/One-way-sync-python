__version__ = '0.0.2'
import time
from datetime import datetime


if __name__ == '__main__':
    Time = datetime.now()
    #while(1):
    for i in range(1,5):
        print i," [ Toy version",__version__,']\t @', Time
        time.sleep(0.5)
