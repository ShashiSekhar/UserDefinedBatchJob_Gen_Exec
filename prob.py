#for Windows only Calculate probability of openening a window
import win32gui
wn=win32gui.GetWindowText (win32gui.GetForegroundWindow())
import time
import datetime
a = []
d ={}
f = open('a.txt','w')
while True:
	curr_win = win32gui.GetForegroundWindow()
	if (wn==win32gui.GetWindowText(curr_win)):
		pass
	else:
		wn=win32gui.GetWindowText(curr_win)
	t = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
	a.append((wn,t))
	if(wn in d.keys()):
   	  	d[wn] = d[wn]+1
   	elif(wn not in d.keys()):
   		d[wn] = 1
   	f.write(str(a))
	time.sleep(5)
	for i in d.keys():
		if d[i] == max(d.values()):
			print(i,"Has max probability")
