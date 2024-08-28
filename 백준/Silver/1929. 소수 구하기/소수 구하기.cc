#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int m, n;
    scanf("%d %d", &m, &n);

    // 2부터 N까지의 모든 자연수를 나열한다

    vector<int> a;
    for (int i = 0; i <= n; i++)
        a.push_back(1);

    a[0] = 0;
    a[1] = 0;

    // 남은 수 중에서 아직 처리하지 않은 가장 작은 수를 찾아 배수를 모두 제거. (가장 작은 수 제외)
    for (int j = 2; j <= n; j++) // 2부터 삭제
    {
        int k = 2;
        if (a[j] != 0) // 아직 제거되지 않은 경우
        {
            while (j * k <= n)
            {
                a[j * k] = 0;
                k++;
            }
        }
    }

    for (int i = m; i <= n; i++)
    {
        if (a[i] == 1)
            printf("%d\n", i);
    }
    return 0;
}
