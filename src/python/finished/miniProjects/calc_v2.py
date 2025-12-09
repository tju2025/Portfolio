#format is:
#number
#operation
#number
x = 0 #variable used to alternate between number and operator 
y = 1 #variable to differ the first calc from subequent ones
z = 0 #the result of the last calculation
o = "" #operator

while True:
  if x == 0:
    try:
      new = input("Number: ") #new number
      try:
        a = float(new)
      except ValueError:
        try:
          if a == int(new):
            pass
        except: 
          raise NameError
      try:
        a = int(new)
      except ValueError:
        pass
      if y == 0:
        print(z, o, a)
        if o == "+":
          z+=a
        if o == "-":
          z-=a
        if o == "*":
          z*=a
        if o == "%":
          z%=a
        if o == "**":
          z**=a
        try:
          if o == "/":
            z/=a
          if o == "//":
            z//=a
        except ZeroDivisionError:
          print("You cannot divide zero")
          break
        print(z)
      elif y == 1: #telling system that this is no longer the first calculation.
        z = a
        y = 0
    except NameError:
      print("Syntax Error, please input a number followed by an operator")
      continue
    x = 1 #switching the binary variable

  list = ["+", "-", "*", "**", "/", "//", "%", "End", "end"]
  if x ==  1:
    try:
      b = input("Operator: ") #new operator
      if b in list:
        o = b #setting the operator to be useable
      else:
        raise ValueError
        continue
      if b == "End":
        break
      if b == "end":
        break
      x=0
    except ValueError:
      print("Syntax Error, please input a known operator followed by a number or \ntype End")
    except SyntaxError:
      print("Syntax Error, please input a known operator followed by a number or \ntype End")