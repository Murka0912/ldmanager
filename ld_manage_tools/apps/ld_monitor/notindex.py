import asyncio
import datetime
import time
async def prin(k):
    for i in range(2):
        k = k ** 1234
    print(k)

def prin1(k):
    for i in range(2):
        k = k **1234
    print(k)

start_time1 = datetime.datetime.now()
r = 0
while r<3:
    r+=1
    asyncio.run(prin(r))
time.sleep(1)
print(datetime.datetime.now()-start_time1)

k=0
start_time = datetime.datetime.now()
print(start_time)
while k<3:
    k+=1
    prin1(k)

time.sleep(1)
print(datetime.datetime.now()-start_time)
r=0
