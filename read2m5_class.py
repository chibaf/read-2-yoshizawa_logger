class read2m5:
#
  def __init__(self):
    import serial
    #read serials
    from read_m5b_class import m5logger
    self.ser0=serial.Serial("/dev/ttyUSB0",115200)
    self.ser1=serial.Serial("/dev/ttyUSB1",115200)
    self.sport0=m5logger()
    self.sport1=m5logger()
 #   
  def reads(self):
    import serial
    from read_m5b_class import m5logger
    array0=self.sport0.read_logger(self.ser0)
    array1=self.sport1.read_logger(self.ser1)
    if array0[0]=='01':
      array=array0[1:11]+array1[1:11]
    elif array0[0]=='02':
      array=array1[1:11]+array0[1:11]
    else:
      array=[0.0]*20;
    return array

