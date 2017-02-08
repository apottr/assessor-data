import urllib,sys,json,time

WAIT_TIME = 0.5

def getParcel(bbl):
	f = urllib.urlopen("http://www.oasisnyc.net/service.svc/lot/"+bbl+"?layerstoselect=")
	return f.read()

def genBbl(borough,block,lot):
	return str(borough)+"0"+str(block).zfill(4)+str(lot).zfill(4)

def update_progress(progress,end,task):
    sys.stdout.write('\r[{0}] {1}/{2}, {3}'.format(('#'*(progress/100)).ljust(end/100), progress,end,task))
    sys.stdout.flush()

def getBlocks(r,borough):
	try:
		f = open('blocks.txt','r')
		a = f.read()
		bl = eval(a)
		print "File found, continuing to parcels \n"
	except IOError:
		bl = []
		for i in range(r):
			d = getParcel(genBbl(borough,i,1))
			if d != '':
				bl.append(i)
				time.sleep(WAIT_TIME)
			update_progress(i,r,"getBlocks")
		f = open('blocks.txt','w')
		f.write(str(bl))
	print 'Done with blocks \n'
	return bl

def getParcels(r,borough,block):
	pl = []
	for i in range(r):
		d = getParcel(genBbl(borough,block,i))
		if d != '':
			pl.append(json.loads(d))
			time.sleep(WAIT_TIME)
		update_progress(i,r,"getParcels")
	f = open('parcels.txt','w')
	f.write(str(pl))
	return pl

def getBorough(r,borough):
	a = getBlocks(r,borough)
	b = {}
	print "Finished retrieving blocks, waiting one minute. \n"
	for i in range(601):
		time.sleep(0.1)
		update_progress(i,600,"waiting")
	print "Done\n"
	for i in range(len(a)):
		b[i] = {}
		c = getParcels(r,borough,a[i])
		for j in range(len(c)):
			b[i][j] = c[j]
		update_progress(i,r,"getBorough")
	return json.dumps(b)

def main():
	f = open('output.txt','w')
	f.write(getBorough(10000,1))
	print("Finished!\n")

main()
