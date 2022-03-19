#include <cstdio>

class Stack
{
private:
  int *stack;
  int top;

public:
  void Push(int data)
  {
    stack[top++] = data;
  }

  int Pop()
  {
    return stack[--top];
  }

  void InitStack(int cap)
  {
    stack = new int[cap];
    top = 0;
  }

  void UninitStack()
  {
    delete[] stack;
  }
};

int main()
{
  Stack st;

  st.InitStack(5);

  st.Push(100); // "st에 push message를 보낸다."
  st.Push(200);
  st.Push(300);

  // st.top = 0; // error -> encapsulation

  printf("Stack => %d\n", st.Pop());
  printf("Stack => %d\n", st.Pop());
  printf("Stack => %d\n", st.Pop());

  st.UninitStack();
}