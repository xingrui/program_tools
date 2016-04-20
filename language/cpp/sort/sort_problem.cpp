#include <iostream>
#include <stdlib.h>
#include <vector>
#include <algorithm>
#include <stdint.h>
using namespace std;

class A {
public:
    A(int32_t k) {
        a = k;
    }
    ~A()
    {};
    int32_t a;
    bool operator < (const A& r) const {
        return a < r.a;

        if (a == r.a)
            return true;
    }
};

static bool comp(const A& l, const A& r)
{
    if (l.a == r.a)
        return true;

    return l.a < r.a;
}
int main()
{
    A t(1);

    vector<A> m;

    for (size_t i = 0; i < 200; i++) {
        m.push_back(t);
    }

    sort(m.begin(), m.end());

    for (size_t i = 0; i < m.size(); i++) {
        cout << m[i].a << " ";
    }

    cout << endl;

    return 0;
}
