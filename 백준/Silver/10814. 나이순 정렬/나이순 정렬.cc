#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool comp(pair<int, string> a, pair<int, string> b)
{
    return a.first < b.first;
}

int main()
{
    int n, age;
    string name;
    vector<pair<int, string>> people;

    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> age >> name;
        people.push_back(make_pair(age, name));
    }

    stable_sort(people.begin(), people.end(), comp); // 나이 오름차순 정렬

    for (const auto &p : people)
        cout << p.first << ' ' << p.second << '\n';

    return 0;
}