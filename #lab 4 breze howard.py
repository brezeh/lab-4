#lab 4 breze howard

#importing os and csv file 
import os
import csv
from datetime import datetime

#variable
keep_going = 'y'

#define the function
def main():
    data = getdata()
    selsort(data)
    insertsort(data)

#getting budget data
def getdata():
    with open("budget_data.csv", "r") as sales: 
        get = csv.reader(sales)
        next(get)
        data = []
        for row in get:
            data.append(row[0])
    return data

#sorting by selection sort
def selsort(data):
    data = [datetime.strptime(date, "%b-%y")for date in data]
    size = len(data)
    for ind in range(size):
        min_index = ind
        for j in range(ind + 1, size):
            if data[j] < data[min_index]:
               min_index = j
            data[ind], data[min_index] = data[min_index], data[ind]
    sorted_dates = [date.strftime("%b-%y") for date in data]
    print('the data after being sorted is:')
    for each in sorted_dates:
        print(each)

#sorting by insertion sort
def insertsort(data):
    data = [datetime.strptime(date, "%b-%y")for date in data]
    size = len(data)
    if size <= 1:
        return
    for i in range(1, size):
        key = data[i]
        j = i=1
        while j >= 0 and key < data[j]:
            data[j+1] = data[j]
            j -= 1
            data[j+1] = key
    sorted_dates = [date.strftime("%b-%y") for date in data]
    print('the data after being sorted is:')
    for each in sorted_dates:
        print(each)
           
#call the function and restart
while keep_going == 'y':
    main()
    keep_going = input ('would you like to run again? ')