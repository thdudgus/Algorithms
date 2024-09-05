#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

vector<int> stack;
vector<int> result;

void push(int x);
void pop();
void size();
void empty();
void top();

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
            scanf("%d", &x);
            push(x);
        }
        else if (!order.compare("pop"))
            pop();
        else if (!order.compare("size"))
            size();
        else if (!order.compare("empty"))
            empty();
        else if (!order.compare("top"))
            top();
    }

    for (auto iter : result)
        printf("%d\n", iter);

    return 0;
}

void push(int x)
{
    stack.push_back(x);
}

void pop()
{
    if (stack.empty())
        result.push_back(-1);
    else
    {
        result.push_back(stack.back());
        stack.pop_back();
    }
}

void size()
{
    result.push_back(stack.size());
}

void empty()
{
    if (stack.empty()) // 비어있으면
        result.push_back(1);
    else
        result.push_back(0);
}

void top()
{
    if (stack.empty()) // 비어있으면
        result.push_back(-1);
    else
        result.push_back(stack.back());
}