#include <cstdio>

struct Stack // "Packing"
{
  int *stack;
  int top; // 0으로 초기화 안 해주어도 되는가?
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