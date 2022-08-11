size=int(input("Enter size of the queue: "))
queue=size*[None]
front=-1
rear=-1

def isFull():
  global rear,size
  return (rear+1)%size==front

def isEmpty():
  global front
  return front==-1

def enqueue(data):
  global front,rear
  if isFull():
    print("The Queue is Full")
  elif front==-1:
    front+=1
    rear+=1
    queue[front]=data
  else:
    rear = (rear + 1) % size
    queue[rear] = data
    
 def dequeue():
   global front,rear
   if isEmpty():
     print("The Stack is Empty\n")
   elif (front==rear):
     temp=queue[front]
     front=-1
     rear=-1
     return temp
   else:
    temp=queue[front]
    front=(front+1)%size
    return temp
  
def viewQueue():
  global front,queue,rear
   if isEmpty():
      print("The Queue is Empty")
   elif rear>=front:
      for i in range(front,rear+1):
        print(queue[i],end=',')
    else:
      for i in range(front, size):
        print(queue[i], end=" ")
      for i in range(0, rear + 1):
        print(queue[i], end=" ")
        print("\n")
        
while (1):
  print("\nOptions:\n1. Enqueue\n2. Dequeue\n3. View Queue\n4. Exit")
  userin=int(input("Enter your choice: "))
  if userin==1:
    data=int(input("Enter data to enqueue: "))
    enqueue(data)
  elif userin==2:
    dequeue()
  elif userin==3:
    viewQueue()
  elif userin==4:
    break
