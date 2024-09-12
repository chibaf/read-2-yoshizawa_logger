def nowtime():
  from datetime import date
  import time
  import serial
  import datetime
  today = date.today()
  t=time.localtime()
  current_time=time.strftime("_H%H_M%M_S%S",t)
  return str(today)+current_time
