import numpy as np
class audio:
    def reshape(self,  depth = 20):
        self.train = np.array([[self.stream[0][y] for y in range(x,depth+x,1)] for x in range(0,len(self.stream[0])-1-depth,depth)])
        self.length = len(self.train)

	def ratio(self):
		self.train_ratio = self.train/self.max
    
    def get_ratio(self):
        self.ratio=self.stream/self.max
        
    def show(self):
        import matplotlib.pyplot as plot
        plot.plot([self.stream[0][i] for i in range(0,len(self.stream),1000)])
        plot.show()
        
    def __init__(self,name = "noise.wav", bit = 16):
        self.max = float (2**(bit-1)-1)
        self.name = name
        from scipy.io.wavfile import read
        from scipy.io.wavfile import write
        content = read(name)
        self.stream = np.transpose(content[1])
        self.get_ratio()

class Xlabel:
    def one_hot(self,i,length):
        x = np.array([0.0 for _ in range(length)])
        x[i] = 1.0
        return x
    def label(self):
        for i,obj in enumerate(self.field):
            obj.labels = np.array([self.one_hot(i,len(self.field)) for _ in range(obj.length)])            
    def add(self,obj):
        self.field.append(obj)
    def __init__(self):
        self.field = []

#loads wave-files, normalizes them, reshape and labeler used to get them in 
#in the right format for training RNN's
#s = audio("Music/love.wav")
#t = audio("Music/stars.wav")
#s.reshape()
#t.reshape()
#
#labeler = Xlabel()
#labeler.add(s)
#labeler.add(t)
#labler.label()
