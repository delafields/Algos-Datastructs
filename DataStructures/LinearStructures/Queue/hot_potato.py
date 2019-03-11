from Queue import Queue

'''
Given an array of names and a number of moves,
return who will we holding the potato when the round ends
'''

def hotPotato(nameList, numMoves):
  q = Queue()

  for name in nameList:
    q.enqueue(name)

  while numMoves > 0:
    temp = q.dequeue()
    q.enqueue(temp)
    numMoves -= 1

  return q.dequeue()


print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],5))
