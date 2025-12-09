def a2():
  if Op2 == '+':
    print(an1+num3)
  if Op2 == '-':
    print(an1-num3)
  if Op2 == '*':
    print(an1*num3)
  if Op2 == '/':
    print(an1/num3)
  if Op2 == '//':
    print(an1//num3)
  if Op2 == '%':
    print(an1%num3)
  if Op2 == '**':
    print(an1**num3) #a stands for add
def s2():
  if Op2 == '+':
    print(sn1+num3)
  if Op2 == '-':
    print(sn1-num3)
  if Op2 == '*':
    print(sn1*num3)
  if Op2 == '/':
    print(sn1/num3)
  if Op2 == '//':
    print(sn1//num3)
  if Op2 == '%':
    print(sn1%num3)
  if Op2 == '**':
    print(sn1**num3) #s stands for subtract
def d2():
  if Op2 == '+':
    print(dn1+num3)
  if Op2 == '-':
    print(dn1-num3)
  if Op2 == '*':
    print(dn1*num3)
  if Op2 == '/':
    print(dn1/num3)
  if Op2 == '//':
    print(dn1//num3)
  if Op2 == '%':
    print(dn1%num3)
  if Op2 == '**':
    print(dn1**num3) #d stands for divide
def m2():
  if Op2 == '+':
    print(mn1+num3)
  if Op2 == '-':
    print(mn1-num3)
  if Op2 == '*':
    print(mn1*num3)
  if Op2 == '/':
    print(mn1/num3)
  if Op2 == '//':
    print(mn1//num3)
  if Op2 == '%':
    print(mn1%num3)
  if Op2 == '**':
    print(mn1**num3) #m stands for multiply
def q2():
  if Op2 == '+':
    print(qn1+num3)
  if Op2 == '-':
    print(qn1-num3)
  if Op2 == '*':
    print(qn1*num3)
  if Op2 == '/':
    print(qn1/num3)
  if Op2 == '//':
    print(qn1//num3)
  if Op2 == '%':
    print(qn1%num3)
  if Op2 == '**':
    print(qn1**num3) #q stands for quotient
def r2():
  if Op2 == '+':
    print(rn1+num3)
  if Op2 == '-':
    print(rn1-num3)
  if Op2 == '*':
    print(rn1*num3)
  if Op2 == '/':
    print(rn1/num3)
  if Op2 == '//':
    print(rn1//num3)
  if Op2 == '%':
    print(rn1%num3)
  if Op2 == '**':
    print(rn1**num3) #r stands for remainder
def p2():
  if Op2 == '+':
    print(pn1+num3)
  if Op2 == '-':
    print(pn1-num3)
  if Op2 == '*':
    print(pn1*num3)
  if Op2 == '/':
    print(pn1/num3)
  if Op2 == '//':
    print(pn1//num3)
  if Op2 == '%':
    print(pn1%num3)
  if Op2 == '**':
    print(pn1**num3)
 #p stands for power
list = ["+", "-", "*", "/", "//", "**", "%", ""] #defining what can be an operator
try:
  num1=int(input("Input number 1: "))
  Op=input("Input operator 1: ")
  if Op not in list:
    raise ValueError
  num2=int(input("Input number 2: "))
  an1=num1+num2
  sn1=num1-num2
  mn1=num1*num2
  dn1=num1/num2
  qn1=num1//num2
  rn1=num1%num2
  pn1=num1**num2
  Op2=input("Input operator 2: ")
  if Op2 not in list:
    raise ValueError
  num3=input("Input number 3: ")
  if num3 != "":
    num3=int(num3)
  if Op == "+":
    if Op2 != "":
      a2()
    else:
      print(an1)

  if Op == "-":
    if Op2 != "":
      s2()
    else:
      print(sn1)

  if Op == "*":
    if Op2 != "":
      m2()
    else:
      print(mn1)

  if Op == "/":
    if Op2 != "":
      d2()
    else:
      print(dn1)

  if Op == "//":
    if Op2 != "":
      q2()
    else:
      print(qn1)

  if Op == "%":
    if Op2 != "":
      r2()
    else:
      print(rn1)

  if Op == "**":
    if Op2 != "":
      p2()
    else:
      print(pn1)



except:
  print("Invalid input.")
  print("""Inputs must be:
  <Number>
  <Operator>
  <Number>
  <Operator> (optional)
  <Number> (required with operator 2)""")