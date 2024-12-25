def RectCalc(w,l):
    area=w*l
    per=2*w+2*l
    return area,per

l1=2
w1=5
area1,per1=RectCalc(w1,l1)
print('Rectangle1 Results: ',area1, per1)
l2=6
w2=4
ara2,per2=RectCalc(w2,l2)
print('Rectangle2 Results: ',area2,per2)