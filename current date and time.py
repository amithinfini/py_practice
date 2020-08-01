from datetime import datetime as dt
now = dt.now()
# print(f'Current date and time is: {now}')
print(now.strftime('Current date and time is: %Y-%m-%d %A, %H:%M:%S'))
input()
