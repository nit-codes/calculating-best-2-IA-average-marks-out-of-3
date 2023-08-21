m1=int(input('Enter the IA 1 marks:'))
m2=int(input('Enter the IA 2 marks:'))
m3=int(input('Enter the IA 3 marks:'))
if m1<=m2 and m1<=m3:
    avg=(m2+m3)/2
elif m2<=m1 and m2<=m3:
    avg=(m1+m3)/2
elif m3<=m1 and m3<=m2:
    avg=(m1+m2)/2
print('The average of best of two IA marks are:',avg)