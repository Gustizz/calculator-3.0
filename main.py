#2*2*2+2
#4 * 2 + 2
#8 + 2
#10


class Math:

  @staticmethod
  def add(x, y):
    return (float(x + y))

  @staticmethod
  def subtract(x, y):
    return (float(x - y))

  @staticmethod
  def divide(x, y):
    return (float(x / y))

  @staticmethod
  def multiply(x, y):
    return (float(x * y))


def revElements(list, index):
  list.pop(index + 1)
  list.pop(index)
  list.pop(index - 1)

  
def SimplifyMultDiv(_equation):

  newEquation = _equation
  
  #Execute mult and div
  i = 0
  while len(newEquation) > i:
  
    if newEquation[i] == "*":
      a = float(newEquation[i - 1])
      b = float(newEquation[i + 1])
  
      revElements(newEquation, i)
      newEquation.insert(i - 1, Math.multiply(a, b))
  
      i = 0
    elif newEquation[i] == "/":
      a = float(newEquation[i - 1])
      b = float(newEquation[i + 1])
  
      revElements(newEquation, i)
      newEquation.insert(i - 1, Math.divide(a, b))
    else:
      i += 1

  return newEquation

  
def SimplifyAddSubOps(_equation):
  
  newEquation = _equation
  #Simplyfy add and sub operators - (+- = -, -- = +)
  i = 0
  while len(newEquation) > i:
    if ((newEquation[i] in basicOps) and (newEquation[i + 1] in basicOps)):
      curOp = newEquation[i]
      nextOp = newEquation[i + 1]
  
      if (curOp == nextOp):
        newEquation[i] = "+"
        newEquation.pop(i + 1)
      else:
        newEquation[i] = "-"
        newEquation.pop(i + 1)
  
      i = 0
    else:
      i += 1

  return newEquation

def SimplifyAddSub(_equation):

  newEquation = _equation
    
  #Execute add and sub
  i = 0
  while len(newEquation) > i:
  
    if newEquation[i] == "+":
      a = float(newEquation[i - 1])
      b = float(newEquation[i + 1])
  
      revElements(newEquation, i)
      newEquation.insert(i - 1, Math.add(a, b))
  
      i = 0
    elif newEquation[i] == "-":
      a = float(newEquation[i - 1])
      b = float(newEquation[i + 1])
  
      revElements(newEquation, i)
      newEquation.insert(i - 1, Math.subtract(a, b))
    else:
      i += 1

  return newEquation

  
# This isolates the values from the operators so multiple digits can be used
  

equation = "(0+"
equation += input("Enter your equation: ")
equation = equation.replace(" ", "")

equation = equation.replace("*", " * ")
equation = equation.replace("/", " / ")
equation = equation.replace("+", " + ")
equation = equation.replace("-", " - ")
equation = equation.replace("(", " ( ")
equation = equation.replace(")", " ) ")
equation += " ) "

sortedEq = []
basicOps = ["+", "-"]

sortedEq = equation.split()




bracketCount = equation.count("(")
x = 0
while bracketCount > x:
  openBrackIndex = 0
  closeBrackIndex = 0
  
  #Find latest open bracket
  for i in range(len(sortedEq)):
    if(sortedEq[i] == "("):
      openBrackIndex = i
  for i in range(len(sortedEq) - 1, 0, -1):
    if(sortedEq[i] == ")"):
      closeBrackIndex = i

  #If openBrack and closeBrack are the same then no brackets are found
  if(openBrackIndex != closeBrackIndex):
    bracketEq = []
    
    for i in range(openBrackIndex + 1, closeBrackIndex, 1):
      bracketEq.append(sortedEq[i])

  
    #print(sortedEq)
    #print(str(openBrackIndex) + " | " + str(closeBrackIndex))
    #print(bracketEq)
      
    bracketEq.insert(0, 0)
    bracketEq.insert(1, "+")
  
    bracketEq = SimplifyMultDiv(bracketEq)
    bracketEq = SimplifyAddSubOps(bracketEq)
    bracketEq = SimplifyAddSub(bracketEq)

    #Removes the old brackets equation from sortedEQ and inserts the simplified value
    for i in range(closeBrackIndex - openBrackIndex + 1):
      sortedEq.pop(openBrackIndex)
      
    sortedEq.insert(openBrackIndex, bracketEq[0])
    x = 0
  else:
    x += 1
  
  
  
    
sortedEq = SimplifyMultDiv(sortedEq)
sortedEq = SimplifyAddSubOps(sortedEq)
sortedEq = SimplifyAddSub(sortedEq)




print("Your result is " + str(sortedEq[0]))
