import time

def insertion_sort(data ,drawData, timeTick):
    for i in range(len(data)):
        temp=data[i]
        j=i-1
        while(j>=0 and data[j]>temp):
            data[j+1]=data[j]
            j-=1
        data[j+1]=temp
        drawData(data, ['green' if j == j-1 or x == j+1 else 'red' for x in range(len(data))])
        time.sleep(timeTick)

    drawData(data, ['green' for x in range(len(data))])
