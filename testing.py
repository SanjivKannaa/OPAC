import csv
from timeit import default_timer as fuck


f = open("bookslist.csv", "r")
content = list(csv.reader(f))
f.close()


t1 = fuck()
l = [i[0] for i in content]
t2 = fuck()
print("time used in the first algo = ", t2)

t1 = fuck()
l = []
for i in content:
    l.append(i[0])
t2 = fuck()




print("fucking time used in the second algo = ", t2)

