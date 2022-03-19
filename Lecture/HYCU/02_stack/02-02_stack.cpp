#include <cstdio>

void Push(int stack[], int &top, int data)
{
  stack[top++] = data;
}

int Pop(int stack[], int &top)
{
  return stack[--top];
}

int main()
{
  int stack1[5];
  int top1 = 0;
  int stack2[5];
  int top2 = 0;

  Push(stack1, top1, 100);
  Push(stack1, top1, 200);
  Push(stack1, top1, 300);

  printf("Stack1 => %d\n", Pop(stack1, top1));
  printf("Stack1 => %d\n", Pop(stack1, top1));
  printf("Stack1 => %d\n", Pop(stack1, top1));

  printf("\n");

  Push(stack2, top2, 200);
  Push(stack2, top2, 400);
  Push(stack2, top2, 600);

  printf("Stack2 => %d\n", Pop(stack2, top2));
  printf("Stack2 => %d\n", Pop(stack2, top2));
  printf("Stack2 => %d\n", Pop(stack2, top2));
}