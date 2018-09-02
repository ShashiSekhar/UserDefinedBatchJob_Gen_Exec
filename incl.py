import time
from pyautogui import *
import sys
import os
import subprocess
comm_list = []
def mvcl(a,b):
	comm_list.append(moveTo(a,b))
	comm_list.append(click())
def p_exit():
	z = ''
	c = 0
	while(c==0):
		z = input('Do you want to save?(Y/n)')
		if z == 'n':
			sys.exit(0)
		elif(z == 'y'):
			c += 1
		else:			
			print('',end='')
	t = input('Name of file: ')
	t += '.py'
	f = open(t,'a+')
	for i in comm_list:
		 f.write(i)
		 f.write('\n')
	sys.exit(0)
def add_prog():
	proc = input("Enter the program : ").strip()
	comm_list.append("print('Launching "+proc+"')")
	p1 = "subprocess.Popen('"+proc+"', stdout=subprocess.PIPE, stderr=subprocess.PIPE)"
	comm_list.append(p1)
	comm_list.append('time.sleep(2)')
def add_text():
	txt = input("Enter text :")
	t1 = "typewrite('"+txt+"',interval=0.1)"
	comm_list.append(t1)
def sel_key():
	print("Select the key")
	print(' 0: Enter \n 1:Tab\n 2:Shift\n 3:Ctrl\n 4:Alt\n 5:Delete\n 6: Other')
	m = int(input())
	if m == 0:
		z ='enter'
	if m == 1:
		z ='tab'
	if m == 2:
		z ='shift'
	if m == 3:
		z ='ctrl'
	if m == 4:
		z ='alt'
	if m == 5:
		z ='del'
	if m == 6:
		z =input('Enter the key code: ').strip()
	return(z)
def add(a):
	if a == '0':
		p_exit()

	if a == '1':
		print("Click on the location to move the cursor to")
		print('place the cursor on position in 5 sec')
		time.sleep(5)
		x,y = position()
		print(x,y)
		comm_list.append("moveTo("+str(x)+','+str(y)+')')

	if a == '2':
		comm_list.append('click()')

	if a == '3':
		print("Click on the location to move the cursor to")
		print('place the cursor on position in 5 sec')
		time.sleep(5)
		x,y = position()
		print(x,y)
		comm_list.append("mvcl("+str(x)+','+str(y)+')')
	if a == '4':
		add_prog()
	if a == '5':
		add_text()
	if a == '6':
		n = input('Enter no. of seconds')
		t = 'time.sleep('+n+')'
		comm_list.append(t)
	if a == '7':
		y = sel_key()
		t = "press('"+y+"')"
		comm_list.append(t)
		comm_list.append('time.sleep(5)')
	if a == '8':
		k = input('The key to press & hold : ')
		t = 'keyDown('+sel_key()+')'
		comm_list.append(t)
	if a == '9':
		k=input('The key to release key:	')
		t = 'KeyUp('+sel_key()+')'
		comm_list.append(t)
	if a == '10':
		n=int(input('The number of keys in command'))
		k = []
		for i in range(0,n):
			k.append(sel_key())
		comm_list.append("hotkey("+','.join(k)+")")
	if a == '11':
		n = input("Enter the amount of Scroll needed:")
		comm_list.append('scroll('+n+')')
	if a == '12':
		comm_list.append('doubleClick()')
	if a == '13':
		comm_list.append(input('Enter the command: ').strip())
	if a == '14':
		if(len(comm_list)>1):
			print(comm_list.pop(-1))
		else:
			print('No previous commands were issued')
	if a == '100':
		print(" 0: Exit\n 1: Move\n 2: Click\n 3: Move and Click\n 4: Add program\n 5: Add Text\n 6: Delay(s)\n 7: Press Key\n 8: Press and hold key\n 9: Release key\n 10: Hotkey input\n 11: Scroll\n 12: Doubleclick\n 13: Other\n 14: Undo\n 100: Help")
	else:
		print('',end='')