#include <cstdio>

int Sum(int s, int e)
{
  int i;
  int sum = 0;

  for (i = s; i <= e; i++)
  {
    sum += i;
  }

  return sum;
}

int main()
{
  printf("sum = %d\n", Sum(1, 10));
  printf("sum = %d\n", Sum(5, 10));
  printf("sum = %d\n", Sum(10, 20));
}

// #include <cstdio>

// int Sum()
// {
//   int i;
//   int sum = 0;

//   for (i = 1; i <= 10; i++)
//   {
//     sum += i;
//   }

//   return sum;
// }

// int main()
// {
//   // int sum = 0;

//   // sum = Sum();

//   // printf("sum = %d\n", sum);
//   printf("sum = %d\n", Sum());
// }

/* 2 ------------------------ */
// #include <cstdio>

// int main()
// {
//   int i;
//   int sum = 0;

//   for (i = 1; i <= 10; i++)
//   {
//     sum += i;
//   }

//   printf("sum = %d\n", sum);
// }

/* 1 ------------------------ */
// #include <cstdio>

// int main()
// {
//   int n = 10;

//   printf("%d\n", n);

//   return 0;
// }
