
def BS(alist, item):
    first = 0
    last = len(alist) - 1
    while first <= last:
        mid = (last + first) // 2
        if alist[mid] == item:
            return True
        if alist[mid] > item:
            last = mid - 1
        else:
            first = mid + 1
    return False

def recursiveBS(list , item):
    if len(list) == 0 :
        return False

    mid = len(list)//2
    if list[mid] == item :
        return True
    if(list[mid] > item):
        return recursiveBS(list[:mid],item)
    else:
        return recursiveBS(list[mid+1:],item)

def bubbleSort(list):
    n = len(list)
    for passLen in range(n-1,0,-1):
        for i in range(passLen):
            if list[i] > list[i+1] :
                list[i],list[i+1] = list[i+1],list[i]

def smartBubbleSort(list):
    n = len(list)
    exchange = True
    for passLen in range(n - 1, 0, -1):
        if exchange == False :
            break
        exchange = False
        for i in range(passLen):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                exchange = True

def selectionSort(list):
    n = len(list)
    for i in range(n-1):
        pos = i
        for j in range(i+1,n):
            if list[j] < list[pos] :
                pos = j
        list[i] , list[pos] = list[pos] , list[i]

def mergeSort(list) :
    if len(list) > 1:
        mid = len(list)//2
        leftList = list[:mid]
        rightList = list[mid:]
        mergeSort(leftList)
        mergeSort(rightList)
        i = 0
        j = 0
        k = 0
        while i < len(leftList) and j < len(rightList):
            if rightList[j] < leftList[i] :
                list[k] = rightList[j]
                j += 1
            else :
                list[k] = leftList[i]
                i += 1
            k += 1
        while i < len(leftList):
            list[k] = leftList[i]
            i += 1
            k += 1
        while j < len(rightList):
            list[k] = rightList[j]
            k += 1
            j += 1

def partition(list,first,last):
    pivotValue = list[first]
    leftMark = first+1
    rightMark = last
    done = False
    while not done :
        while leftMark <= rightMark and list[leftMark] < pivotValue :
            leftMark += 1
        while rightMark >= leftMark and list[rightMark] > pivotValue:
            rightMark -= 1
        if rightMark < leftMark :
            done = True
        else :
            list[leftMark] ,list[rightMark] = list[rightMark],list[leftMark]
    list[first],list[rightMark] = list[rightMark],list[first]
    return rightMark

def quickSortHelper(list,first,last):
    if(first<last):
        splitPoint = partition(list,first,last)
        quickSortHelper(list,first,splitPoint-1)
        quickSortHelper(list,splitPoint+1,last)

def quickSort(list):
    quickSortHelper(list,0,len(list)-1)


class Stack:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items == []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

class Queue:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items == []
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)


class Node:
    def __init__(self,initData):
        self.data = initData
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,newData):
        self.data = newData
    def setNext(self,newNext):
        self.next= newNext

class UnorderedList:
    def __init__(self):
        self.head=None
    def isEmpty(self):
        return self.head==None
    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    def length(self):
        current = self.head
        count = 0
        while current != None :
            count += 1
            current = current.getNext()
        return  count
    def search(self,item):
        current = self.head
        while current != None:
            if current.getData() == item :
                return True
            current = current.getNext()
        return False
    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None :
            self.head = current.getNext
        else:
            previous.setNext(current.getNext())

class OrderedList:
    def __init__(self):
        self.head=None
    def isEmpty(self):
        return self.head==None
    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None :
            self.head = current.getNext
        else:
            previous.setNext(current.getNext())
    def length(self):
        current = self.head
        count = 0
        while current != None :
            count += 1
            current = current.getNext()
        return  count
    def search(self,item):
        current = self.head
        while current != None :
            if current.getData() == item :
                return  True
            elif current.getData() > item :
                break
            else :
                current = current.getNext()
        return False
    def add(self,item):
        current = self.head
        previous = None
        while current != None :
            if current.getData() > item :
                break
            else:
                current = current.getNext()
        temp = Node(item)
        if previous == None :
            temp.setNext(self.head)
            self.head = temp
        else :
            temp.setNext(current)
            previous.setNext(temp)

class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.right = None
        self.left = None
    def insertLeft(self,newNode):
        if self.left == None :
            self.left = newNode
        else:
            t = BinaryTree(newNode)
            t.left = self.left
            self.left = t
    def insertRight(self,newNode):
        if self.right == None :
            self.right = newNode
        else :
            t = BinaryTree(newNode)
            t.right = self.right
            self.right = t
    def getRootVal(self):
        return self.key
    def setRootVal(self,obj):
        self.key = obj
    def getLeftChild(self):
        return self.left
    def getRightChild(self):
        return self.right

class BSTNode:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        self.size = 0
    def length(self):
        return self.size
    def has_key(self,key):
        return self.bstSearch(self.root,key) is not None
    def bstSearch(self,subtree,target):
        if subtree is None :
            return None
        if target < subtree.key :
            return self.bstSearch(subtree.left,target)
        if target > subtree.key :
            return self.bstSearch(subtree.right,target)
        return subtree
    def bstMinimum(self,subtree):
        if (subtree is None) or (subtree.left is None) :
            return subtree
        return self.bstMinimum(subtree.left)
    def bstMaximum(self,subtree):
        if (subtree is None) or (subtree.right is None) :
            return subtree
        return self.bstMaximum(subtree.right)
    def add(self,key,value):
        node = self.bstSearch(self.root,key)
        if node is not None :
            node.value = value
            return False
        self.root = self.bstInsert(self.root,key,value)
        self.size += 1
        return True
    def bstInsert(self,subtree,key,value):
        if subtree is None:
            subtree = BSTNode(key, value)
        elif key < subtree.key:
            subtree.left = self.bstInsert(subtree.left,key,value)
        else:
            subtree.right = self.bstInsert(subtree.right, key, value)
        return subtree
    def remove(self,key):
        node = self.bstSearch(self.root,key)
        assert node is not None, "Invalid Key."
        self.root = self.bstRemove(self.root,key)
        self.size -= 1
    def bstRemove(self,subtree,target):
        if target < subtree.key :
            subtree.left = self.bstRemove(subtree.left,target)
            return subtree
        elif target > subtree.right :
            subtree.right = self.bstRemove(subtree.right,target)
            return subtree
        else :
            if subtree.left is None and subtree.right is None :
                return None
            elif subtree.left is None :
                return subtree.right
            elif subtree.right is None :
                return subtree.left
            else :
                successor = self.bstMinimum(subtree.right)
                subtree.value = successor.value
                subtree.key = successor.key
                subtree.right = self.bstRemove(subtree.right,successor.key)
                return subtree


