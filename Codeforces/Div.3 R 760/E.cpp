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
    ll n; cin >> n;
    vector <ll> b(n), a(n);
    ll sb = 0, sa;
    for (auto &i : b) {
        cin >> i;
        sb+=i;
    }
    if (sb%(n*(n+1)/2)) {
        cout << "NO";
        return;
    }
    sa = sb/(n*(n+1)/2);
    for (int i = 0; i < n; i++) {
        ll cur = sa+b[(i+n-1)%n]-b[i];
        if (cur <= 0 || cur%n) {
            cout << "NO";
            return;
        }
        a[i] = cur/n;
    }
    cout <<"YES" << '\n';
    for (auto &i : a) {
        cout << i << ' ';
    }
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
