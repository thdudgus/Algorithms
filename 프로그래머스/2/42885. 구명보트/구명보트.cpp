#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> people, int limit)
{

    // 구명보트에 가장 가벼운 사람과 무거운 사람을 태우고 가능하면 둘을 태우고, 불가능하면 무거운 사람만 태우는 방법
    int answer = 0;
    int i = 0;
    sort(people.begin(), people.end());
    while (i < people.size())
    {
        if (people[i] + people[people.size() - 1] <= limit)
        {
            ++i;
            people.pop_back();
            ++answer;
        }
        else
        {
            people.pop_back();
            ++answer;
        }
    }

    return answer;
}

int main()
{
    vector<int> s = {70, 80, 50, 50};
    int limit = 100;
    int answer = solution(s, limit);
    printf("%d", answer);
    return 0;
}