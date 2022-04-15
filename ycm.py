import random as r
t=10000
ct=0
change=0
not_change=0
for i in range(t):
    a = r.randint(0,2)
    g = r.randint(0,2)
    if a==g:not_change=not_change+1
    else:change=change+1
    ct=ct+1
print('运行',t,'次后，不换选对的概率为',not_change/ct,'，换后选对的概率为',change/ct)
