class m5logger:
    
  def read_logger(self,ser):
    import serial
    line = ser.readline()
    try:
      line2=line.strip().decode('utf-8')
    except UnicodeDecodeError:
      return [0.0]*11
    data = [str(val) for val in line2.split(",")]
    data1=[]
    if len(data)==12:
      for i in range(0,11):
        try:
          if i==0:
            data1.append(data[0])
          else:
            fd=float(data[i+1])
            data1.append(fd)
        except:
          return [0.0]*11
    else:
      return [0.0]*11
    return data1