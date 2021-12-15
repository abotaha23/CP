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

// const int dx[8]={0, 0, 1, -1, 1, -1, -1, 1}, dy[8]={1, -1, 0, 0, 1, -1, 1, -1}, M = 1e9+7, M2 = 998244353;

void burn()
{
    int n, k; cin >> n >> k;
    vector <int> a(n);
    for (auto &i : a) cin >> i;
    sort(a.begin(), a.end());
    int sc = 0;
    for (int i = 0; i < n-2*k; i++) {
        sc += a[i];
    }
    int meq = 0, cur[(int)2e5+10] = {0};
    for (int i = n-2*k; i < n; i++) {
        ++cur[a[i]];
        if (cur[a[i]] > meq) meq = cur[a[i]];
    }
    sc+=(meq-k > 0 ? meq-k : 0);
    cout << sc;
}

int main()
{
    Taha_on_da_code
    int t = 1; cin >> t;
    while(t--) {
        burn();
        cout << '\n';
    }
    return 0;
}
