#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <cmath>
using namespace std;

static bool comp(pair<int, int> &a, pair<int, int> &b)
{
    return a.second > b.second;
}

int main()
{
    int n;
    double input;
    vector<int> number;
    double sum = 0;
    scanf("%d", &n);
    map<int, int> frequency;

    for (int i = 0; i < n; i++)
    {
        scanf("%lf", &input);
        number.push_back((int)input);                       // 수 입력
        sum += input;                                  // 수들의 총합
        frequency.insert({(int)input, frequency[input]++}); // 최빈값 구하기 위한 map
    }

    sort(number.begin(), number.end()); // 오름차순 정렬

    vector<pair<int, int>> v(frequency.begin(), frequency.end()); // 최빈값 구하기 위한 map을 vector로 변환
    sort(v.begin(), v.end(), comp);                                  // 최빈값 오름차순 정렬
    bool same = false;                                               // 최빈값이 여러개인가
    for (int i = 1; i < v.size(); i++)
    {
        if (v[0].second == v[i].second)
        {
            same = true;
            break;
        }
    }

    double avg = round((sum / (double)n));
    if (avg == -0)
        avg = 0;

    printf("%.0lf\n", avg);                            // 산술평균
    printf("%d\n", number[n / 2]);                  // 중앙값
    printf("%d\n", same ? v[1].first : v[0].first); // 최빈값
    printf("%d\n", number.back() - number.front()); // 범위

    return 0;
}