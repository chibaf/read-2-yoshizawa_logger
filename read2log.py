from datetime import date
import time
import matplotlib.pyplot as plt
import serial
import datetime
import os

from read_m5_class import m5logger

path = './go_read2log.txt'
today = date.today()
t=time.localtime()
current_time=time.strftime("_H%H_M%M_S%S",t)
fn="SL_"+str(today)+current_time+".csv"
f=open(fn,'w',encoding="utf-8")
start = time.time()

ser0=serial.Serial("/dev/ttyUSB0",115200)
ser1=serial.Serial("/dev/ttyUSB1",115200)
sport0=m5logger()
sport1=m5logger()

fl=open("read2log_log.txt",'a',encoding="utf-8")
t_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(t_delta, 'JST')
now = datetime.datetime.now(JST)
d = now.strftime('%Y %m %d %H:%M:%S')
s1=d+": read2log.py started\n"
fl.write(s1)
while True:
  is_file = os.path.isfile(path)
  if is_file:
    array0=sport0.read_logger(ser0)
    array1=sport1.read_logger(ser1)
    if array0[0]=='01':
       array=array0[1:10]+array1[1:10]
    else:
      array=array1[1:10]+array0[1:10]
      f.write(str(array)+'\n')
  else:
    t_delta = datetime.timedelta(hours=9)
    JST = datetime.timezone(t_delta, 'JST')
    now = datetime.datetime.now(JST)
    d = now.strftime('%Y %m %d %H:%M:%S')
    s1=d+": read2log.py stopped\n"
    fl.write(s1)
    fl.close()
    f.close()
    exit()