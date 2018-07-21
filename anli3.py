import time
import sys

# length=19
# count=1
# while True:
#     print('\r%s@%s' % ('#' * (count-1),'#' * (length-count)),end='')
#
#     time.sleep(0.3)
#     if count==length:
#         count=0
#     count+=1



length1=30
count1=1

while True:

        print('\r%s@%s'%('*'*(count1-1), '#' *(length1-count1)),end='')
        try:
            time.sleep(0.1)
        except KeyboardInterrupt:
            print("\nBye-bye")
            break
        if count1==length1:
            count1=0
        count1+=1




