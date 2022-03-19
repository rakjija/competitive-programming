#include <cstdio>

int stack[5];
int top = 0;

void Push(int data)
{
  stack[top++] = data;
}

int Pop()
{
  return stack[--top];
}

int main()
{
  Push(100);
  Push(200);
  Push(300);

  printf("%d\n", Pop());
  printf("%d\n", Pop());
  printf("%d\n", Pop());
}