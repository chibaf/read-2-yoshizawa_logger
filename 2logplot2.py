from datetime import date
import time
import matplotlib.pyplot as plt
import serial
import datetime
import os
# read logger class
from read_m5b_class import m5logger
from mplot_class import mplot

#read serials
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
#
path = './go_2log.txt' # flag file
#
today = date.today()
t=time.localtime()
current_time=time.strftime("_H%H_M%M_S%S",t)
fn="2L_"+str(today)+current_time+".csv"
f=open(fn,'w',encoding="utf-8")
# plot arrary
splot=mplot(20)
#
start = time.time()
#
while True:
  t_delta = datetime.timedelta(hours=9)
  JST = datetime.timezone(t_delta, 'JST')
  now = datetime.datetime.now(JST)
  d = now.strftime('%Y %m %d %H:%M:%S.%f')
  is_file = os.path.isfile(path) # check flag file
  if is_file: # file was found
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
    splot.plot(array)
  else: # flag not found
    s1=d+": read2log.py stopped\n"
    fl.write(s1)
    fl.close()
    f.close()
    exit()