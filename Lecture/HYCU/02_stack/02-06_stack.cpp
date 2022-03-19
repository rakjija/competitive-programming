#include <cstdio>

class Stack
{
public:
  int *stack;
  int top;
};

void Push(Stack &st, int data)
{
  st.stack[st.top++] = data;
}

int Pop(Stack &st)
{
  return st.stack[--st.top];
}

void InitStack(Stack &st, int cap)
{
  st.stack = new int[cap];
  st.top = 0;
}

void UninitStack(Stack &st)
{
  delete[] st.stack;
}

int main()
{
  Stack st;

  InitStack(st, 5);

  Push(st, 100);
  Push(st, 200);
  Push(st, 300);

  printf("Stack => %d\n", Pop(st));
  printf("Stack => %d\n", Pop(st));
  printf("Stack => %d\n", Pop(st));

  UninitStack(st);
}