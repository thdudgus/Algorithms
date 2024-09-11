#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    unsigned int k, n, input; // 이미 가지고 있는 랜선의 개수 // 필요한 랜선의 개수 // (입력값,)랜선을 잘랐을 때의 개수 합.
    scanf("%d %d", &k, &n);
    vector<int> lan; // 랜선의 길이, 나눈 몫 저장
    for (int i = 0; i < k; i++)
    {
        scanf("%d", &input);
        lan.push_back(input);
    }
    sort(lan.begin(), lan.end());

    unsigned int ans = 0; // 최대값 임시저장 및 답
    unsigned int left = 1;
    unsigned int right = lan.back();
    unsigned int mid = (left + right) / 2;

    while (left <= right)
    {
        mid = (left + right) / 2;
        input = 0; // 랜선을 잘랐을 때의 개수 합.

        for (int i = 0; i < k; i++) // 랜선을 나눈 몫들 (개수 구하기 위함)
            input += lan[i] / mid;  // 랜선들을 a의 길이로 잘랐을 때 나오는 랜선 개수

        if (input < n) //  자르는 기준이 너무 커서 줄여야 함.
            right = mid - 1;
        else  // 자르는 기준이 너무 작아서 늘려야 함.
        {
            left = mid + 1;
            ans = max(ans, mid);  // 최댓값을 구하기 위함.
        }
    }

    printf("%d", ans);

    return 0;
}