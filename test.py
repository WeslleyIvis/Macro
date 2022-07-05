import time

current_time = time.localtime()
timestamp = time.strftime("%I:%m:%S")
print(timestamp)

# for i in range(5):
#   time.sleep(1)
#   print(time.localtime())
