#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int N, input;
    scanf("%d", &N);
    vector<float> score;
    float total, temp, temp2;

    for (int i = 0; i < N; i++)
    {
        scanf("%d", &input);
        score.push_back(input);
    }

    sort(score.begin(), score.end());
    temp = score[N-1];
    total = 0;

    for (int i = 0; i < N ; i++)
    {
        temp2 = (score[i] / temp) * 100;
        score[i] = temp2;
        total += score[i];
    }

    printf("%.2f", (float)(total/N));

    return 0;
}