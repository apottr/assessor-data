import sys,time
'''
def update_progress(progress,end,task):
    sys.stdout.write('\r[{0}] {1}/{2}, {3}'.format(('#'*(progress/100)).ljust(end/100), progress,end,task))
    sys.stdout.flush()

for i in range(10000):
	time.sleep(0.01)
	update_progress(i,10000,"task50")

print
'''
try:
	f = open('blcks.txt','r')
	if f:
		a = f.read()
		a = eval(a)
		print(isinstance(a,list))
		print(a[0])
except IOError:
	print('File not found, continuing')