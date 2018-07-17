sum100=0
counter=0
while counter<100:
    counter+=1
    if counter %2:
        continue
    sum100 +=counter
print(sum100)

sum50=0
counter_1=0
while counter_1<=99:
    counter_1+=1
    if counter_1%2==0:
        continue
    sum50+=counter_1
print(sum50)