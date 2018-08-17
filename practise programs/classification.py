import random
from matplotlib import pyplot as plt
import math
from numpy import exp

ip=[[1,1],[1.5,.5],[2,1],[1.5,1.5],[1,2],[2,2.5],[4,4],[4.5,4.5],[5,5],[4,6],[4.5,4],[5.5,4]]
op=[[0],[0],[0],[0],[0],[0],[1],[1],[1],[1],[1],[1]]
learning_rate=0.01
t0=random.randint(0,9)
t1=random.randint(0,9)
t2=random.randint(0,9)
temp0=0
temp1=0
temp2=0
xv=[]
yv=[]

def sigmoid(x):
	return (1/(1+exp(-x)))

def cost(k,y):
		if y==0:
			return -(math.log(1-sigmoid(k)))
		else:
			return -(math.log(sigmoid(k)))

sm=0

for _ in range(0,10000):
	for x in range(0,12):
		theta=t0+t1*ip[x][0]+t2*ip[x][1]
		y=op[x]
		single_cost=cost(theta,y)
		sm=sm+single_cost

	total_cost=sm/2
	if _%500==0:
		yv.append(total_cost)
		xv.append(_)

	sm=0
	for x in range(0,12):
		theta=t0+t1*ip[x][0]+t2*ip[x][1]
		hypo=(sigmoid(theta)-op[x])
		sm=sm+hypo

	temp0=t0-(learning_rate/12)*sm


	sm=0
	for x in range(0,12):
		theta=t0+t1*ip[x][0]+t2*ip[x][1]
		hypo=(sigmoid(theta)-op[x])*ip[x][0]
		sm=sm+hypo

	temp1=t1-(learning_rate/12)*sm


	sm=0
	for x in range(0,12):
		theta=t0+t1*ip[x][0]+t2*ip[x][1]
		hypo=(sigmoid(theta)-op[x])*ip[x][1]
		sm=sm+hypo

	temp2=t2-(learning_rate/12)*sm
	t0=temp0
	t1=temp1
	t2=temp2
	print(t0,t1,t2)

plt.plot(xv,yv)
plt.xlabel("iterations")
plt.ylabel("cost")
plt.show()

op=1
while(op==1):
	op=int(input("enter 1 for testing or 0 for exit"))
	if op==0:
		continue
	a=float(input("Enter for a:"))
	b=float(input("Enter for b:"))
	test=t0+t1*a+t2*b
	test=sigmoid(test)
	print("for ",a," for ",b," y is ",round(test[0]))


