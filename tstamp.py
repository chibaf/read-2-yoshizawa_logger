def timestamp():
  from datetime import date
  import datetime
  t_delta = datetime.timedelta(hours=9)
  JST = datetime.timezone(t_delta, 'JST')
  now = datetime.datetime.now(JST)
  rd = now.strftime('%Y %m %d %H:%M:%S.%f')
  return rd
  