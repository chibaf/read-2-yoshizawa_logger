class mplot:

  def __init__(self, num):
    self.num=num
    data0=[0]*self.num
    self.data=[data0]*10
    self.x=range(0, 10, 1)
    
  def plot(self,array):
    import matplotlib.pyplot as plt
    self.array=array
    self.data.pop(-1)
    self.data.insert(0,self.array)
    rez = [[self.data[j][i] for j in range(len(self.data))] for i in range(len(self.data[0]))]
    plt.figure(100)
    plt.clf()
    plt.ylim(-25,40)
    tl=[0]*20
    hl=[]
    for i in range(0,self.num):
      tl[i],=plt.plot(self.x,rez[i],label="T"+str(i))
    for i in range(0,self.num):
      hl.append(tl[i])
    plt.legend(handles=hl)
    plt.pause(0.1)