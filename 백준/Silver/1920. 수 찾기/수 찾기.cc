#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool binSearch(const vector<int>& A, int low, int high, int target);

int N, M, input;
vector<int> A;
vector<int> B;

int main()
{
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        cin >> input;
        A.push_back(input);
    }
    sort(A.begin(), A.end());

    cin >> M;
    for (int i = 0; i < M; i++)
    {
        cin >> input;
        B.push_back(input);
    }

    for (int i = 0; i < M; i++) // B 요소가 A에 있는지 찾기
    {
        bool found = binSearch(A, 0, N - 1, B[i]);
        if (found)
            cout << "1\n";
        else
            cout << "0\n";
    }

    return 0;
}

bool binSearch(const vector<int>& A, int low, int high, int target)
{
    if (low > high)
        return false;

    int mid = (low + high) / 2;
    if (A[mid] == target)
        return true;
    else if (A[mid] < target)
        return binSearch(A, mid + 1, high, target);
    else
        return binSearch(A, low, mid - 1, target);
}
