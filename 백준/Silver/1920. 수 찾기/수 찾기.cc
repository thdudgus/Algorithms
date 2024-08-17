#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int N, M, input;
    vector<int> A;
    vector<int> B;

    scanf("%d", &N);
    for (int i = 0; i < N; i++)
    {
        scanf("%d", &input);
        A.push_back(input);
    }
    sort(A.begin(), A.end());

    scanf("%d", &M);
    for (int i = 0; i < M; i++)
    {
        scanf("%d", &input);
        B.push_back(input);
    }

    bool found;
    for (int i = 0; i < M; i++)
    {
        int left = 0;
        int right = M; 
        int mid = (left + right) / 2;
        found = false;
        while (left <= right)  
        {
            mid = (left + right) / 2;
            if (A[mid] == B[i])
            {
                found = true;
                break; // 반복문을 빠져나감.
            }
            else if (A[mid] > B[i]) // 찾으려는 수가 더 작음. A의 왼쪽으로 mid 이동
                right = mid - 1;
            else if (A[mid] < B[i]) // 찾으려는 수가 더 큼. A의 오른쪽으로 mid 이동
                left = mid + 1;
                }
        printf(found ? "1\n" : "0\n");
    }

    return 0;
}