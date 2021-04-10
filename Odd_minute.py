from datetime import datetime
import random
import time

for i in range(5):
    right_this_minute = datetime.today().minute
    odd_minute = right_this_minute%2
    int(odd_minute)
    if odd_minute == 0:
        print( "This minute seems a little odd.")
    else:
        print("Not a odd minute.")
    print(datetime.today().minute)
    wait_time = random.randint(1,60)
    time.sleep(wait_time)
