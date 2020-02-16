nr=0
for i in range(0,100):
  if(i%2==0):
    nr=nr+i 
    continue
  elif(i<10):
    print(i)
  elif(i>10 and i<20):
    continue