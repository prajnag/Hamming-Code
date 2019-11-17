from functools import reduce
from random import choice
import socket
import math
from tkinter import *
#from tkinter import messagebox

def no_error():
    n=entry_1.get()
    #print(n)
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    port = 1234
    s.connect(('127.0.0.1',port))
    #s.send(str(0).encode())
    s.send(str(hen(n,0)).encode())
    s.close()

def error_1():
	n=entry_1.get()
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	port = 1234
	s.connect(('127.0.0.1',port))
	#s.send(str(1).encode())
	s.send(str(hen(n,1)).encode())
	s.close()

def hen(string,val):
	#print("entered")
	bi = bin(int.from_bytes(string.encode(), 'big'))
	binary = bi[2:]
	#print(str(binary)+" "+ str(format(len(str(binary)))))
	r = 0
	while (2**r < r+ len(str(binary)) +1):
		r = r+1
	encode = str(binary)
	for i in range(r):
		encode = encode[:(2**i)-1] + "0" + encode[(2**i)-1:]
		arr = [int(i) for i in encode]
	for i in range(r):
		index = [x for x in range(len(encode)) if ((x+1)&(2**i))]
		arr[(2**i)-1] = reduce(lambda x,y:((x^y) and 1 or 0),[arr[j] for j in index])
	arr = list(map(lambda x:str(x),arr))
	hcode = ''.join(arr)
	if val==1:
		#print(hcode)
		hcode = onebit(hcode)
		#print(hcode)
	return hcode

def onebit(string):
	arr = [int(x) for x in string]
	i = choice(range(len(arr)))
	arr[i] = 0 if arr[i]==1 else 1
	new_arr = [str(x) for x in arr]
	return ''.join(new_arr)


root=Tk()
root.configure(background='pink')
root.geometry('700x400')
root.title('Client')

label_0=Label(root,text="MESSAGE TO SERVER:",width=20)
label_0.place(x=90,y=53)


entry_1=Entry(root)
entry_1.place(x=300,y=53)

button_0=Button(root,text="No error",command=no_error)
button_0.place(x=90,y=180)
button_1=Button(root,text="1 bit error",command=error_1)
button_1.place(x=180,y=180)
root.mainloop()

