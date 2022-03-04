import datetime

d_1 = datetime.datetime(2020, 5, 17 , 23 ,  4 , 3)
d_2=datetime.datetime.now()
sub=d_2-d_1

print(sub.total_seconds())
