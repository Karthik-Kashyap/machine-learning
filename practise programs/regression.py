import random
from matplotlib import pyplot as plt

ip=[1,2,3,6]
op=[1,2,3,6]
t1=random.randint(0,9)
t2=random.randint(0,9)
sm=0
xv=[]
yv=[]

learning_rate=0.01
for z in range(0,10000):
	for x in range(0,3):
		hypo=t1+t2*ip[x]
		dif=hypo-op[x]
		sm=sm+(dif*dif)

	cost=sm/6


	for x in range(0,3):
		hypo=t1+t2*ip[x]
		dif=hypo-op[x]
		sm=sm+dif
	sm=sm/3
	temp1=t1-learning_rate*sm
	
	for x in range(0,3):
		hypo=t1+t2*ip[x]
		dif=hypo-op[x]
		sm=sm+dif*ip[x]
	sm=sm/3
	temp2=t2-learning_rate*sm

	t1=temp1
	t2=temp2
	test=5
	if z%10==0:
		k=t1+t2*test
		print("theta=",t1,t2,round(k))
	if z%1000==0:
		yv.append(t1)
		xv.append(t2)
		x1=1
		y1=t1+t2*x1
		x2=10
		y2=t1+t2*x2
		plt.plot([x1,x2],[y1,y2])
		plt.show()
plt.plot(xv,yv)
plt.xlabel("t2")
plt.ylabel("t1")
plt.show()



for x in range(0,2):
		theta=t0+t1*ip[x][0]+t2*ip[x][1]
		y=op[x]
		single_cost=cost(theta,y)
		sm=sm+single_cost

	total_cost=sm/2