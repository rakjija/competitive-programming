#include <cstdio>

class Stack
{
private:
  int *stack;
  int top;
  int capacity;

public:
  /* ----------------- Deep Copy ----------------- */
  Stack(const Stack &arg) // COPY CONSTRUCTOR(복사 생성자)
  {
    stack = new int[capacity = arg.capacity];
    top = arg.top;

    for (int i = 0; i < top; i++)
    {
      stack[i] = arg.stack[i];
    }
  }

  const Stack &operator=(const Stack &arg) // 복사 대입 연산자
  {
    return *this;
  }
  /* --------------------------------------------- */

  Stack(int cap) // CONSTRUCTOR(생성자)
  {
    capacity = cap;
    stack = new int[cap];
    top = 0;
  }

  ~Stack() // DESTRUCTOR(소멸자)
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
  Stack st1(1000);

  st1.Push(100);
  st1.Push(200);
  st1.Push(300);

  Stack st2 = st1; // 복사 대입 연산자 = 복사 생성자 + 대입 연산자

  printf("Stack1 => %d\n", st1.Pop());
  printf("Stack1 => %d\n", st1.Pop());
  printf("Stack1 => %d\n", st1.Pop());

  printf("\n");

  printf("Stack2 => %d\n", st2.Pop());
  printf("Stack2 => %d\n", st2.Pop());
  printf("Stack2 => %d\n", st2.Pop());
}