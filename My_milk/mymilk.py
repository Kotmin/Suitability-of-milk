from time import gmtime, strftime
import time

days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
today =time.strftime("%A")
def check(days):
    if days==today:
        return True
    else:
        return False
def find_index(i):
    for x in range(7):
        if check(days[i])==True:
            return i
        else:
            i+=1
       


index_of_current_day = find_index(0)
print(index_of_current_day)

