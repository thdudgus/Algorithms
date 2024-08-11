#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
using namespace std;

bool compare(string a, string b);

int main()
{
    int n; // 입력받는 문자의 개수
    cin >> n;
    string w;
    set<string> wordSet;    // 중복 체크를 위한 set
    int wordSize[51] = {0}; // 문자열의 길이는 최대 50, wordSize[0]은 필요 x

    cin.ignore();
    for (int i = 0; i < n; i++)
    {
        getline(cin, w);
        if (wordSet.find(w) == wordSet.end()) // 중복이 아닐 경우에만 글자별 개수 1 증가
        {
            ++wordSize[w.size()];
            wordSet.insert(w); // set에 추가하여 중복 체크, set은 중복을 허용하지 않고 자동정렬 해줌.
        }
    }

    vector<string> word(wordSet.begin(), wordSet.end());  // set을 vector<string>으로 복사.

    sort(word.begin(), word.end(), compare);  // 문자열 길이 기준 정렬

    int begin = 0;
    for (int i = 0; i <= 51; i++) // 가질 수 있는 문자열 길이 배열만큼 반복
    {
        if (wordSize[i] > 1)   // wordSize의 각 배열 크기가 1 초과일 때만 사전식 정렬.
            sort(word.begin() + begin, word.begin() + begin + wordSize[i]);

        begin = begin + wordSize[i]; // 정렬을 시작할 인덱스 갱신
    }

    for (const auto &w : word) // word 벡터에 저장된 모든 문자열을 출력.
        cout << w << endl;

    return 0;
}

bool compare(string a, string b)
{
    return a.size() < b.size();
}