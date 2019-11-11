import numpy as np
i=0
j = 0
map = []
o = []
while i <= 60 :
    if j > 60 :
        j = 60
    while j <= 60:
        map.append([i,j])
        j += 2
    i += 2
for i in range(20):
    x=np.random.randint(0,60)
    y=np.random.randint(0,90)
    o.append([x,y])
