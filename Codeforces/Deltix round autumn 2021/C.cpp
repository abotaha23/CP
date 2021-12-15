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

const int dx[8]={0, 0, 1, -1, 1, -1, -1, 1}, dy[8]={1, -1, 0, 0, 1, -1, 1, -1}, M = 1e9+7, M2 = 998244353;

bool primes[1000100];

void burn()
{
    int n, e; ll ans = 0; cin >> n >> e;
    vector <int> a(n), pos_p;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        if (primes[a[i]]) pos_p.push_back(i);
    }
    for (auto &cur_p : pos_p) {
        int cur_p2 = cur_p;
        ll cnt1 = 0, cnt2 = 0;
        while(cur_p >= e && a[cur_p-e] == 1) {
            cnt1++; cur_p-=e;
        }
        while(cur_p2+e < n && a[cur_p2+e] == 1) {
            cnt2++; cur_p2+=e;
        }
        ans+=cnt1+cnt2+cnt2*cnt1;
    }
    cout << ans;
}

int main()
{
    Taha_on_da_code
    memset(primes, true, sizeof primes);
    primes[0] = primes[1] = false;
    for (int i = 2; i*i < 1000001; i++) {
        for (int j = i*i; j < 1000001; j+=i)
            primes[j] = false;
    }
    int t = 1; cin >> t;
    while(t--) {
        burn();
        cout << '\n';
    }
    return 0;
}
