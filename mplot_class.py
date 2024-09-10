class mplot:

  def __init__(self, num):
    self.num=num
    data0=[0]*self.num
    data=[data0]*10
    x=range(0, 10, 1)
    
  def plot(self,y):
    data.pop(-1)
    data.insert(0,array)
    rez = [[data[j][i] for j in range(len(data))] for i in range(len(data[0]))]
    plt.figure(100)
    plt.clf()
    plt.ylim(-25,40)
    tl=[0]*20
    hl=[]
    for i in range(0,num):
      tl[i],=plt.plot(x,rez[i],label="T"+str(i))
    for i in range(0,num):
      hl.append(tl[i])
    plt.legend(handles=hl)
    plt.pause(0.1)