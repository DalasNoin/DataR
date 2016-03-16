import numpy as np
class noise:
    
    def append_raw(self,values):
        for value in values:
            self.packed_values.append(struct.pack('h',value))
    
    def append(self,frequency, length = 1, relativ_volume = 1):
        volume = 32767 * relativ_volume
        zeta = self.sr * 2 / frequency / np.pi
        values = [int(np.sin(x/zeta)*volume) for x in range (int(self.sr * 2/frequency))]
        values = np.resize(values,(length*self.sr*2,))
        for value in values:
            self.packed_values.append(struct.pack('h',value))
        
    def save(self):
        value_stream = b''.join(self.packed_values)
        noise = wave.open(self.name,'w')
        noise.setparams((self.p1,self.p2,self.sr,self.p4,'NONE','not compressed'))
        noise.writeframes(value_stream)
        noise.close()
    
    def __init__(self, sr = 44100,name = "noise.wav"):
        self.sr=sr
        self.p1=2
        self.p2 = 2
        self.p4 = 0
        self.name = name
        self.packed_values = []