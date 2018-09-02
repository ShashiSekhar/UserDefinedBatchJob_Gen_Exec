from incl import *
print('Launching firefox')
subprocess.Popen('firefox', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
time.sleep(2)
mvcl(568,122)
typewrite('youtube.com',interval=0.1)
time.sleep(5)
mvcl(841,186)
typewrite('pokemon',interval=0.1)
