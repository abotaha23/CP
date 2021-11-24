#include <iostream>
#include <chrono>
#include <string>
#include <sstream>
#include <cmath>
#include <iomanip>
#include <cstring>
#include <string>
#include <algorithm>
#include <array>
#include <vector>
#include <deque>
#include <set>
#include <unordered_set>
#include <map>
#include <queue>

typedef long long ll;
#define Taha_on_da_code ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

using namespace std;

void burn()
{
    int n, i, a, b; cin >> n >> a >> b;
    deque <int> ans;
    ans.push_front(a); ans.push_back(b);
    for (i = n; ans.size() < n/2+1; i--) {
        if (i == b || i == a) continue;
        if (i < a) {
            cout << -1 << endl;
            return;
        }
        ans.push_front(i);
    }
    if (i==a) i--;
    for ( ;  i <= b && i; i--) {
        if (i == a || i == b) continue;
        ans.push_back(i);
    }
    if (ans.size() < n) {
        cout << -1 << endl;
        return;
    }
    for (auto &k : ans) {
        cout << k << ' ';
    }
    cout << endl;
}

int main()
{
    Taha_on_da_code;
    int t = 1; cin >> t;
    while(t--) burn();
    return 0;
}

