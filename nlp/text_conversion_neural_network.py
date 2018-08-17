import numpy as np
import time
start_time = time.time()

'''	DATA PREPROCESSING TO MATCH THE NEURAL NETWORK
The letters are converted into numbers
for example:a is 1, b is 2 ...... z is 26.
To generalize the numbers I have divided them by 26 to get values of letters
between 0 and 1. For ex: a is 0.038461538461538464

The Y values or the labels is a one hot list which is a list of 26 elements.
If the output character should be 'b' then the list will have
[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
'''

original_file=open("original",'r').read()
cipher_file=open("cipher","r").read()
test="abcde"
'''
for x in range(100):
	print(original_file[x])
'''
cipher_file=[e.lower() for e in cipher_file if e not in {' ','\n'}]
original_file=[e.lower() for e in original_file if e not in {' ','\n'}]


original_list=[]
for x in original_file[0:26]:
	y=ord(x)-96
	y/=26
	#print(y)
	z=[]
	z.append(y)
	original_list.append(z)

one_hot_list=[]
for x in cipher_file[0:26]:
	y=[0]*26
	z=ord(x)-97
	y[z]=1
	one_hot_list.append(y)

#for x,y in zip(original_list,one_hot_list):
#	print(x,y)



### DATA PREPROCESSING ENDS


def nonlin(x,deriv=False):
	if(deriv==True):
		return x*(1-x)

	return 1/(1+np.exp(-x))

x=np.array(original_list)
y=np.array(one_hot_list)

#np.random.seed(1)

syn0=2*np.random.random((1,13))-1
syn1=2*np.random.random((13,26))-1
#syn2=2*np.random.random((15,26))-1

for j in range(0,100000000):
	l0=x
	l1=nonlin(np.dot(l0,syn0))
	l2=nonlin(np.dot(l1,syn1))
	#l3=nonlin(np.dot(l2,syn2))

	l2_error=y-l2

	if j%10000000==0 :
		print("error:"+str(np.mean(np.abs(l2_error))))
		#print("l2:"+str(len(l2)))
		#print("l2_error:"+str(len(l2_error)))

	#l3_delta=l3_error*nonlin(l3,deriv=True)
	#l2_error=l3_delta.dot(syn2.T)
	l2_delta=l2_error*nonlin(l2,deriv=True)
	l1_error=l2_delta.dot(syn1.T)
	l1_delta=l1_error*nonlin(l1,deriv=True)


	#syn2+=l2.T.dot(l3_delta)
	syn1+=l1.T.dot(l2_delta)
	syn0+=l0.T.dot(l1_delta)


print("learning over\n")
while(1):
	test="abcdefghijklmnopqrstuvwxyz"
	test_list=[]
	for x in test:
		#print("x="+x)
		y=ord(x)-96
		y/=26
		#print(y)
		z=[]
		z.append(y)
		test_list.append(z)
		#print("test="+str(test_list[0]))

	#print("\n\n"+str(test_list)+"\n\n")
	print("testing...")
	#print("input:",test_list)
	output_str=""
	for x in test_list:
		l0=x
		l1=nonlin(np.dot(l0,syn0))
		l2=nonlin(np.dot(l1,syn1))
		#l3=nonlin(np.dot(l2,syn2))
		#print("output for input is")
		#print(l2)
		l=list(l2)
		m=max(l)
		m=l.index(m)
		ch=m+97
		ch=str(chr(ch))
		output_str+=ch
	print("\nabcdefghijklmnopqrstuvwxyz\nbcdefghijklmnopqrstuvwxyza\n"+output_str)
	#i=int(input("1)input-------0)exit"))
	#if i==0:
	print("--- %s seconds ---" % (time.time() - start_time))
	exit()
