class Calculator:
  def isNum(self, str):
    try:
      float(str)
      return True
    except:
      return False

  def printNum(self, str): 
    return lambda: self.label.setText("%s%s" % (self.label.text(), str))
    
  def clearLabel(self): 
      self.label.clear()
      self.operation = 0

  def root(self):
      label_value = self.label.text()
      if not self.operation:
        self.label.setText("%s √ " % (label_value))
        self.operation = 5
  
  def backspace(self):
      label_value = self.label.text()
      if label_value:
        if (self.isNum(label_value.split()[-1])):
          self.label.setText(label_value[:-1])
        else:
          self.label.setText(label_value[:-3])
          self.operation = 0
  
  def equal(self):
      operations = [
        lambda a, b: a + b,
        lambda a, b: a - b,
        lambda a, b: a * b,
        lambda a, b: a / b,
        lambda a, b: b ** (1/a)
      ]

      label_value = self.label.text()
      items = label_value.split()

      if (len(items) > 2 and self.isNum(items[-1])):
        if (self.isNum(items[0])):
          a = float(items[0])
          if (self.isNum(items[2])):
            b = float(items[2])
          else:
            b = -float(items[3])
        elif (self.isNum(items[1])):
          a = -float(items[1])
          if (self.isNum(items[3])):
            b = float(items[3])
          else:
            b = -float(items[4])
        res = operations[self.operation - 1](a, b)
      elif self.operation == 5 and self.isNum(items[-1]):
        a = 2
        b = float(items[1])
        res = operations[4](a, b)
      else:
        if (self.isNum(items[0])):
          res = float(items[0])
        elif (len(items) > 1 and self.isNum(items[1])):
          res = -float(items[1])
        else:
          res = ""
      
      if (self.isNum(res)):
        if (round(res, 0) == res):
          res = int(round(res, 0))
        else:
          res = ".".join([str(res).split(".")[0], str(res).split(".")[1][:10]])
      self.label.setText(str(res))
      self.operation = 0

  def divide(self):
    label_value = self.label.text()
    if (not self.operation and label_value and self.isNum(label_value[-1])):
      self.label.setText(label_value + " / ")
      self.operation = 4

  def multiply(self):
      label_value = self.label.text()
      if (not self.operation and label_value and self.isNum(label_value[-1])):
        self.label.setText(label_value + " * ")
        self.operation = 3

  def subtract(self):
      label_value = self.label.text()
      if (not label_value):
        self.label.setText(" - ")
      elif (not self.operation and self.isNum(label_value.split()[-1])):
        self.label.setText(label_value + " - ")
        self.operation = 2
      elif (self.operation in [1, 3, 4] and self.isNum(label_value.split()[-2])):
        self.label.setText("%s- " % (label_value))
      elif (self.operation == 2 and label_value.split()[-1] == "-"):
        self.label.setText("%s + " % (label_value[:-3]))
        self.operation = 1

  def point(self):
      label_value = self.label.text()
      if (label_value and label_value.split()[-1].find(".") < 0 and self.isNum(label_value[-1])):
        self.label.setText("%s." % (label_value))

  def add(self):
      label_value = self.label.text()
      if (not self.operation and label_value and self.isNum(label_value[-1])):
        self.label.setText(label_value + " + ")
        self.operation = 1