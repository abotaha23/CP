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

vector <int> par, cap, mcap;

int fp (int ch)
{
    if (par[ch] == ch) return ch;
    return fp(par[ch]);
}

bool jo (int i, int j)
{
    i = fp(i); j = fp(j);
    if (i == j) return false;
    if (cap[i] < cap[j]) swap(i, j);
    cap[i]+=cap[j];
    cap[j] = 0;
    par[j] = i;
    return true;
}

void burn()
{
    int n, d, ex = 0; cin >> n >> d;
    par.resize(n+1);
    for (int i = 1; i <= n; i++) {
        par[i] = i;
    }
    cap.assign(n+1, 1);
    while(d--) {
        int f, t;
        cin >> f >> t;
        ex+=!jo(f, t);
        mcap = cap;
        sort(mcap.rbegin(), mcap.rend());
        int ans = -1;
        for (int i = 0; i <= ex; i++) {
            ans+=mcap[i];
        }
        cout << ans << '\n';
    }
}

int main()
{
    Taha_on_da_code
    int t = 1; // cin >> t;
    while(t--) {
        burn();
        cout << '\n';
    }
    return 0;
}
