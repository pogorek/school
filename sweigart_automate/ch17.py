# 17 KEEPING TIME, SCHEDULING TASKS, AND LAUNCHING PROGRAMS17 KEEPING TIME, SCHEDULING TASKS, AND LAUNCHING PROGRAMS
import datetime, time

#! The time Module
## The time.time() Function

# import time
# time.time()
# print('time.time(): ', time.time())
# # 1543813875.3518236
# x = (time.time() - 1543813875.3518236) / 60 / 60 / 24 / 365
# print(x)


# import time
# def calcProd():
#     # Calculate the product of the first 100,000 numbers.
#     product = 1
#     for i in range(1, 100000):
#         product = product * i
#     return product

# startTime = time.time()
# prod = calcProd()
# endTime = time.time()
# print('The result is %s digits long.' % (len(str(prod))))
# print('Took %s seconds to calculate.' % (endTime - startTime))


# import time
# print(time.ctime())
# # 'Mon Jun 15 14:00:38 2020'
# thisMoment = time.time()
# print(time.ctime(thisMoment))
# # 'Mon Jun 15 14:00:45 2020'

## The time.sleep() Function

# import time
# for i in range(3):
#     print('Tick')
#     time.sleep(1)
#     print('Tock')
#     time.sleep(1)

## Rounding Numbers

# import time
# now = time.time()
# print(now)
# # 1543814036.6147408
# print(round(now, 2))
# # 1543814036.61
# print(round(now, 4))
# # 1543814036.6147
# print(round(now))
# # 1543814037

## Project: Super Stopwatch

#! The datetime Module
# import datetime
# print(datetime.datetime.now())
# # 2022-07-06 00:56:28.409890
# dt = datetime.datetime(2019, 10, 21, 16, 29, 0, 666)
# print(dt)
# # 2019-10-21 16:29:00.000666
# print(dt.year, dt.month, dt.day)
# # (2019, 10, 21)
# print(dt.hour, dt.minute, dt.second)
# # (16, 29, 0)

# import datetime, time
# print(datetime.datetime.fromtimestamp(1000000))
# # 1970-01-12 14:46:40
# print(datetime.datetime.fromtimestamp(time.time()))
# # 2022-07-06 00:58:30.280009

# import datetime
# halloween2019 = datetime.datetime(2019, 10, 31, 0, 0, 0)
# newyears2020 = datetime.datetime(2020, 1, 1, 0, 0, 0)
# oct31_2019 = datetime.datetime(2019, 10, 31, 0, 0, 0)
# print(halloween2019 == oct31_2019) # True
# print(halloween2019 > newyears2020) # False
# print(newyears2020 > halloween2019) # True
# print(newyears2020 != oct31_2019) # True

## The timedelta Data Type

# delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
# print(delta.days, delta.seconds, delta.microseconds)
# # (11, 36548, 0)
# print(delta.total_seconds())
# # 986948.0
# print(str(delta))
# # '11 days, 10:09:08'

# # calculate the date 1,000 days from now
# dt = datetime.datetime.now()
# print(dt)
# # 2022-07-06 01:11:02.181184
# thousandDays = datetime.timedelta(days=1000)
# print(dt + thousandDays)
# # 2025-04-01 01:11:02.181184

# timedelta objects can be added or subtracted with datetime objects or other timedelta objects using the + and - operators. 
# A timedelta object can be multiplied or divided by integer or float values with the * and / operators
oct21st = datetime.datetime(2019, 10, 21, 16, 29, 0)
aboutThirtyYears = datetime.timedelta(days=365 * 30)
print(oct21st)
# 2019-10-21 16:29:00
print(oct21st - aboutThirtyYears)
# 1989-10-28 16:29:00
print(oct21st - (2 * aboutThirtyYears))
# 1959-11-05 16:29:00

## Pausing Until a Specific Date