from datetime import date
import time
import matplotlib.pyplot as plt
import serial
import datetime
import os

from read_m5b_class import m5logger

path = './go_2log.txt'
today = date.today()
t=time.localtime()
current_time=time.strftime("_H%H_M%M_S%S",t)
fn="2L_"+str(today)+current_time+".csv"
f=open(fn,'w',encoding="utf-8")
start = time.time()

ser0=serial.Serial("/dev/ttyUSB0",115200)
ser1=serial.Serial("/dev/ttyUSB1",115200)
sport0=m5logger()
sport1=m5logger()

fl=open("2log_log.txt",'a',encoding="utf-8")
t_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(t_delta, 'JST')
now = datetime.datetime.now(JST)
d = now.strftime('%Y %m %d %H:%M:%S.%f')
s1=d+": read2log.py started\n"
fl.write(s1)
data0=[0]*20
data=[data0]*10
x=range(0, 10, 1)
while True:
  t_delta = datetime.timedelta(hours=9)
  JST = datetime.timezone(t_delta, 'JST')
  now = datetime.datetime.now(JST)
  d = now.strftime('%Y %m %d %H:%M:%S.%f')
  is_file = os.path.isfile(path)
  if is_file:
    array0=sport0.read_logger(ser0)
    array1=sport1.read_logger(ser1)
    if array0[0]=='01':
      array=array0[1:11]+array1[1:11]
    elif array0[0]=='02':
      array=array1[1:11]+array0[1:11]
    else:
      array=[0.0]*20;
    temps=""
    for i in range(0,19):
      temps=temps+str(array[i])+","
    temps=temps+str(array[19])
    ttime=time.time()-start
    if ttime<0.001:
      ttime=0.0
    ttime=round(ttime,5)
    f.write(d+","+str(ttime)+","+str(temps)+'\n')
# plot
    data.pop(-1)
    data.insert(0,array)
    rez = [[data[j][i] for j in range(len(data))] for i in range(len(data[0]))]
    plt.figure(100)
    plt.clf()
    plt.ylim(-25,40)
    tl=[0]*20
    hl=[]
    for i in range(0,20):
      tl[i],=plt.plot(x,rez[i],label="T"+str(i))
    for i in range(0,20):
      hl.append(tl[i])
    plt.legend(handles=hl)
    plt.pause(0.1)
  else:
    s1=d+": read2log.py stopped\n"
    fl.write(s1)
    fl.close()
    f.close()
    exit()