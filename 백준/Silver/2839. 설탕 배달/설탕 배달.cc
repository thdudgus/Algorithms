#include <iostream>
using namespace std;

int main()
{
    int N, fr, tr, temp, total, total1, total3;
    scanf("%d", &N);
    fr = N % 5; // 5로 나눈 나머지
    tr = N % 3; // 3으로 나눈 나머지

    if (fr == 0) // 5로 나누어 떨어지면
    {
        total = N / 5;
        printf("%d", total);
        return 0;
    }
    else
    {
        for (int i = N / 5; i >= 1; i--)
        {
            if ((N - (5 * i)) % 3 == 0)
            {
                total1 = (N - 5 * i) / 3;
                temp = N - (total1 * 3);
                total = total1 + temp / 5;
                printf("%d", total);
                return 0;
            }
        }
    }
    if (tr == 0) // 3으로 나누어 떨어지면
        total = N / 3;
    else
        total = -1;
    printf("%d", total);
    return 0;
}