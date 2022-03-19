#include <cstdio>

class Stack
{
private:
  int *stack;
  int top;

public:
  Stack(int cap) // CONSTRUCTOR
  {
    stack = new int[cap];
    top = 0;
  }

  ~Stack() // DESTRUCTOR
  {
    delete[] stack;
  }

  void Push(int data)
  {
    stack[top++] = data;
  }

  int Pop()
  {
    return stack[--top];
  }
};

int main()
{
  Stack st(1000);

  st.Push(100);
  st.Push(200);
  st.Push(300);

  printf("Stack => %d\n", st.Pop());
  printf("Stack => %d\n", st.Pop());
  printf("Stack => %d\n", st.Pop());
}