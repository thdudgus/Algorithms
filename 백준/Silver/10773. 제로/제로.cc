#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int main()
{
    int k, input;
    int total = 0;
    vector<int> z;
    scanf("%d", &k);

    for (int i = 0; i < k; i++)
    {
        scanf("%d", &input);
        if (input == 0)
            z.pop_back();
        else
            z.push_back(input);
    }

    for (int i = 0; i < z.size(); i++)
        total += z[i];

    printf("%d", total);
    return 0;
}