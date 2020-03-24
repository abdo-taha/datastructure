#include <bits/stdc++.h>


using namespace std;

template <typename T>
struct NodeStack{
    T data;
    NodeStack<T> * Next = nullptr;
};


template <typename T>
class StackLL{
private:
    NodeStack<T> * pTop = nullptr;
    int Size = 0;
public:
    bool isEmpty();
    void push(T value);
    T pop();
    T peek();
    int getSize();
    void Clear();
    ~StackLL(){
        Clear();
    }


};

template <typename T>
bool StackLL<T>::isEmpty(){
    return this->Size == 0;
}

template <typename T>
void StackLL<T>::push(T value){
    NodeStack<T> *pNode = new NodeStack<T>;
    //NodeStack<T> *pNode = (NodeStack<T> *) malloc(sizeof(NodeStack<T>));
    pNode->data = value;
    pNode->Next = pTop;
    pTop = pNode;
    ++Size;
}

template <typename T>
T StackLL<T>::pop(){
    NodeStack<T> *pTemp = pTop;
    pTop = pTop->Next;
    T tempValue = pTemp->data;

    delete pTemp;
   // free(pTemp);
   --Size;
    return  tempValue;

}

template <typename T>
T StackLL<T>::peek(){
    return pTop->data;
}

template <typename T>
int StackLL<T>::getSize(){
    return Size;
}

template <typename T>
void StackLL<T>::Clear(){
    NodeStack<T> *pTemp ;
    while(pTop!=nullptr){
        pTemp = pTop;
        pTop = pTop->Next;
        delete pTemp;
    }
    Size = 0;

}






int main()
{
//
//    StackLL<int> s ;
//    s.push(1);
//    s.push(2);
//    cout << s.peek()<<endl;
//    cout << s.getSize()<<endl;
//   // int a = s.pop();
//
//    cout<< s.pop()<< " " ;
//    cout << s.pop()<<endl;
//    s.push(5);
//    s.Clear();
//    s.push(6);
//    cout << s.peek() << " "<<s.getSize();





    return 0;
}
