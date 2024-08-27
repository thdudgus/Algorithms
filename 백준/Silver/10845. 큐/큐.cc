#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

vector<int> queue;
vector<int> result;

void push(int x);
void pop();
void size();
void empty();
void front();
void back();

int main()
{
    int n, x;
    string order;

    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        cin >> order;

        if (!order.compare("push"))
        {
            cin >> x;
            push(x);
        }
        else if (!order.compare("pop"))
            pop();
        else if (!order.compare("size"))
            size();
        else if (!order.compare("empty"))
            empty();
        else if (!order.compare("front"))
            front();
        else if (!order.compare("back"))
            back();
    }

    for (auto iter : result)
        cout << iter << endl;

    return 0;
}

void push(int x)
{
    queue.push_back(x);
    return;
}

void pop()
{
    if (queue.empty())
        result.push_back(-1);
    else
    {
        result.push_back(queue.front());
        queue.erase(queue.begin());
    }
    return;
}

void size()
{
    result.push_back(queue.size());
    return;
}

void empty()
{
    if (queue.empty()) // 비어있으면
        result.push_back(1);
    else
        result.push_back(0);
    return;
}

void front()
{
    if (queue.empty())
        result.push_back(-1);
    else
        result.push_back(queue.front());
    return;
}

void back()
{
    if (queue.empty())
        result.push_back(-1);
    else
        result.push_back(queue.back());
    return;
}