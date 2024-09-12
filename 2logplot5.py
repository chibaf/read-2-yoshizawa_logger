from datetime import date
import time
import serial
import datetime
import os
#
from mplot_class import mplot
import tstamp
import nowtime
from read2m5_class import read2m5

fl=open("2log_log.txt",'a',encoding="utf-8")
s1=tstamp.timestamp()+": read2log.py started\n"
fl.write(s1)
#
path = './go_2log.txt' # flag file
#
fn='2L_'+nowtime.nowtime()+".csv"
f=open(fn,'w',encoding="utf-8")
# plot class
splot=mplot(20)
# initial time
start = time.time()
#
read2log=read2m5()
while True:
  is_file = os.path.isfile(path) # check flag file
  if is_file: # file was found
    array=read2log.reads()
    temps=""
    for i in range(0,19):
      temps=temps+str(array[i])+","
    temps=temps+str(array[19])
    ttime=time.time()-start
    if ttime<0.001:
      ttime=0.0
    ttime=round(ttime,5)
    f.write(tstamp.timestamp()+","+str(ttime)+","+str(temps)+'\n')
# plot
    splot.plot(array)
  else: # flag not found
    s1=tstamp.timestamp()+": read2log.py stopped\n"
    fl.write(s1)
    fl.close()
    f.close()
    exit()