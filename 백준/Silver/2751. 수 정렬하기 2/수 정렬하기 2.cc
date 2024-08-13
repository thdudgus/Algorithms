#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    vector<int> number;
    int n, m;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        cin >> m;
        number.push_back(m);
    }

    sort(number.begin(), number.end());

    for (auto &n : number)
        printf("%d\n", n);

    return 0;
}