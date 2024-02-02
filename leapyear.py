year = int(input('Year to Check: '))
if year%400==0 or year%100!=0 and year%4==0:
   print("LEAP")
else:
   print("NOT LEAP")
