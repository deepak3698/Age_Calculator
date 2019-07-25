from datetime import datetime
a=str(datetime.now().date())

list1=a.split("-")
list1=list(map(int,list1))
list1=list1[::-1]

print("please enter your birthday")
bd_year=int(input("Year:"))
bd_month=int(input("Month(1-12):"))
bd_day=int(input("Date(day):"))

if(bd_month>12 or bd_day>31):
    print("Invalid Input")
else:
    list2 = [bd_day, bd_month, bd_year]
    if(list1[0]<list2[0]):
        list1[0]=list1[0]+30
        list1[1]=list1[1]-1

    if(list1[1]<list2[1]):
        list1[1]=list1[1]+12
        list1[2]=list1[2]-1

    day=list1[0]-list2[0]
    month=list1[1]-list2[1]
    year=list1[2]-list2[2]
    print(f"you are {year} year {month} month {day} day old")
