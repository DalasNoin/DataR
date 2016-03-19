import numpy as np

class Symbol:
    import Image

    Y = np.array(None)
    name="default"
    
    def show(self):
        height=300
        img = self.Image.new( 'RGB', (self.Y.shape[0]), "black")
        maxi=max(Y[1])
        height_ratio=height/maxi
        pixels=img.load()
        for i in range(self.Y.shape[0]):
            pixels[i][int(Y[1]*height_ratio)]="red"
        img.show()


class Stock(Symbol):
	from StringIO import StringIO
	import urllib2
	import datetime
	
	dates=[]
	path = "storage/"
	verbose = True

	def show(self):
		import matplotlib.pyplot as plt
		plt.plot(self.Y[0][::-1])
		plt.show()

	def save(self,text):
		text_file= open("%s%s.cvs"%(self.path,self.name),'w')
		text_file.write(text)
		text_file.close()
		
	def get_vol(self):
		return ((self.Y[3]-self.Y[0])/self.Y[3])
	
	def fetch(self):
		import time

		#get date
		date = self.datetime.datetime.now()

		start=time.time()
		down_location = "http://real-chart.finance.yahoo.com/table.csv?s=%s&d=%d&e=%d&f=%d&g=d&a=%d&b=%d&c=%d&ignore=.csv" %(self.name,self.end_date.month-1,self.end_date.day-1,self.end_date.year,self.start_date.month-1,self.start_date.day-1,self.start_date.year)	
		content = self.urllib2.urlopen(down_location)
		
		#self.save(content.read())
		self.Y=np.genfromtxt(self.StringIO(content.read()),delimiter=',',skip_header = 1)
		self.Y = self.Y[::-1]
		self.Y= (np.transpose(self.Y)[1:7])
		if self.verbose:
			print down_location
			print "Fetched in %f seconds" % (time.time()-start)
	
	def __init__(self,name="GOOG",start_date=None,end_date=None,verbose=True):
		self.verbose = verbose
		if start_date == None:
			self.start_date = self.datetime.datetime(1962,1,3)
		else:
			self.start_date = start_date
		if end_date == None:
			self.end_date = self.datetime.datetime.now()
		else:
			self.end_date = end_date
		self.name=name
		self.fetch()

