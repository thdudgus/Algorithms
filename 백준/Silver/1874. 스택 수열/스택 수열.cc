#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n, temp;
    vector<int> sequence; // 목표 수열
    vector<int> st;       // 1~n 저장할 벡터
    vector<char> result;  // +, -를 저장할 벡터

    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &temp);
        sequence.push_back(temp); // 주어진 수열 저장
    }

    temp = 1; // 1~n 스택에 푸시한 후, 값 저장.(pop한 후, pop한 수의 다음부터 push하기 위함.)

    for (int i = 0; i < n; i++)
    { // 수열 하나씩 탐색
        while (sequence[i] >= temp)
        {
            st.push_back(temp); // 1~n 스택에 push
            result.push_back('+');
            temp++; // 마지막으로 push한 수 기억.
        }
        if (sequence[i] == st.back())
        {
            st.pop_back();
            result.push_back('-');

            if (i + 1 < n && sequence[i + 1] < st.back())
            {
                printf("NO");
                return 0;
            }
        }
    }

    for (int i = 0; i < result.size(); i++)
        printf("%c\n", result[i]);

    return 0;
}