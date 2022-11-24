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
  list.pop(i + 1)
  list.pop(i)
  list.pop(i - 1)


equation = input("Enter your equation: ")
equation = equation.replace(" ", "")

sortedEq = []
ops = ["+", "-"]

for x in equation:
  sortedEq.append(x)


#10*2
#[0, + ,1, 0, *, 2]
#[0, +, "10", *, 2]



#Execute mult and div
i = 0
while len(sortedEq) > i:

  if sortedEq[i] == "*":
    a = float(sortedEq[i - 1])
    b = float(sortedEq[i + 1])

    revElements(sortedEq, i)
    sortedEq.insert(i - 1, Math.multiply(a, b))

    i = 0
  elif sortedEq[i] == "/":
    a = float(sortedEq[i - 1])
    b = float(sortedEq[i + 1])

    revElements(sortedEq, i)
    sortedEq.insert(i - 1, Math.divide(a, b))
  else:
    i += 1

#Simplyfy add and sub operators - (+- = -, -- = +)
i = 0
while len(sortedEq) > i:
  if ((sortedEq[i] in ops) and (sortedEq[i + 1] in ops)):
    curOp = sortedEq[i]
    nextOp = sortedEq[i + 1]

    if (curOp == nextOp):
      sortedEq[i] = "+"
      sortedEq.pop(i + 1)
    else:
      sortedEq[i] = "-"
      sortedEq.pop(i+1)

    i = 0
    print(sortedEq)
  else:
    i += 1
    
#Execute add and sub
i = 0
while len(sortedEq) > i:

  if sortedEq[i] == "+":
    a = float(sortedEq[i - 1])
    b = float(sortedEq[i + 1])

    revElements(sortedEq, i)
    sortedEq.insert(i - 1, Math.add(a, b))

    i = 0
  elif sortedEq[i] == "-":
    a = float(sortedEq[i - 1])
    b = float(sortedEq[i + 1])

    revElements(sortedEq, i)
    sortedEq.insert(i - 1, Math.subtract(a, b))
  else:
    i += 1

print("Your result is " + str(sortedEq[0]))
