import socket
from functools import reduce
import math
from tkinter import *

def hde(string):
	arr = [int(x) for x in string]
	r = [i for i in range(1,len(arr)+1) if math.log(i,2)%1.0==0]
	darr = []
	for j in r:
		index = [i for i in range(len(arr)) if (i+1)&j]
		dbit = reduce(lambda x,y:(x^y),[arr[k] for k in index])
		darr.append(j*dbit)
	value = reduce(lambda x,y:x+y,darr)
	status(value)
	if value == 0:
		new_str = [str(arr[i]) for i in range(len(arr)) if i+1 not in r]
	else:
		#print("Error detected and corrected")
		#print(arr)
		arr[value-1] = 0 if arr[value-1]==1 else 1
		new_str = [str(arr[i]) for i in range(len(arr)) if i+1 not in r]
	hdecode = ''.join(new_str)	
	newstr ="0b"+hdecode
	n = int(newstr,2)
	n=n.to_bytes((n.bit_length()+7)//8,'big').decode()
	return n

def status(code):
	if code == 0:
		msg = "Error free message"
	else:
		msg = "One bit error detected at " + str(code) + "th position."
	label_3 = Label(root,text=msg)
	label_3.place(x=300,y=180)

def data():
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
	#val=1
	#print("Socket successfully created.")
	port = 1234
	s.bind(('',port))
	s.listen(5)
	c, addr = s.accept()
	#val=c.recv(4)
	#val=int(val)
	data=c.recv(1024)
	data=data.decode()
	#print(data)
	data=hde(str(data))
	label_1=Label(root,text=data)
	label_1.place(x=300,y=53)
	#print("data is",data)
	#s.listen(10)
	c.close()
	#s.close()

root=Tk()
root.configure(background='pink')
root.title('Server')
root.geometry('700x400')
root.after(1000,data)

label_0=Label(root,text="MESSAGE FROM CLIENT:",width=20)
label_0.place(x=90,y=53)
#label_3=Label(root,text="ERROR",width=20)
#label_3.place(x=90,y=200)


label_2=Label(root,text="ERROR MESSAGE:",width=20)
label_2.place(x=90,y=180)
#c.close()
root.mainloop()




    
