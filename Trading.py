import numpy as np

class picture:
	import Image
	pixels = np.array(None)
	label = 0

	def random_normal(self):
		size = self.pixels.shape[0]**2
		pixels = np.random.normal(size)
		pixels = np.reshape(self.pixels,[size ** 0.5, size ** 0.5])

	def random_empty(self):
		self.random_normal()
		for i in range(self.pixels.shape[0]):
			self.pixels[0][i]=0
	
	def __init__(self,width=28,height=28,label = 0):
		self.pixels = np.zeros([width,height],"float")	
		self.label = label
		if label == 0:
			random_normal()
		elif label == 1:
			random_empty()

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
	star_year=1962
	path = "storage/"

	def save(self,text):
		text_file= open("%s%s.cvs"%(self.path,self.name),'w')
		text_file.write(text)
		text_file.close()
		
	
	def fetch(self):
		import time

		#get date
		date = self.datetime.datetime.now()

		start=time.time()
		content = self.urllib2.urlopen("http://real-chart.finance.yahoo.com/table.csv?s=%s&d=1&e=%d&f=%d&g=d&a=0&b=2&c=%d&ignore=.csv" %(self.name,date.month-1,date.day,date.year,self.start_year))
		
		#self.save(content.read())
		self.Y=np.genfromtxt(self.StringIO(content.read()),delimiter=',',skip_header = 1)
		self.Y= np.transpose(np.transpose(self.Y)[1:7])
		print "Fetched in %f seconds" % (time.time()-start)
	
	def __init__(self,name="GOOG",start_year=1962):
		self.start_year=start_year
		self.name=name
		self.fetch()

