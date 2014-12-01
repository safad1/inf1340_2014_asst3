__author__ = 'http://stackoverflow.com/questions/17016731/python-finding-the-average-stock-value-for-each-month'


lis = [("2013-02-12", 200.0), ("2012-02-25", 300.0), ("2000-03-04", 100.0), ("2000-03-05", 50.0)]
dic = {}
for date, val in lis:
    #split the date string at '-' and assign the first  2 items to  year,month
    year, month = date.split('-')[:2]
    #now check if (month,year) is there in the dict
    if (month, year) not in dic:
        #if the tuple was not found then initialise one with an empty list
        dic[month,year] = []

    dic[month,year].append(val)# append val to the (month,year) key

print (dic)
#Now iterate over key,value items and do some calculations to get the desired output
sol = []
for key, val in dic.items():
    new_key = "-".join(key)
    avg = sum(val) / len(val)
    sol.append((avg, new_key))
print (sol)