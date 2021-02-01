import time
from concurrent.futures import ThreadPoolExecutor

def returnnumber(a):
    time.sleep(1)
    return a

# print(returnnumber(56))


start=time.time()

with ThreadPoolExecutor(max_workers=3) as executor:
    for result in executor.map(returnnumber,range(100)):
        print("Count:", result)

print('total time =', time.time()-start)




input()
