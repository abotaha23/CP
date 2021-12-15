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

vector <vector <int>> adj; vector <bool> vis;

void dfs(int cur)
{
    vis[cur] = true;
    for (auto &i: adj[cur]) {
        if (!vis[i]) dfs(i);
    }
}

void burn()
{
    int n; cin >> n;
    adj.assign(n+1, {});
    vis.assign(n+1, false);
    vector <bool> cur(n+1, false);
    bool flag = false;
    for (int i = 1, a; i <= n; i++) {
        cin >> a;
        if (cur[a]) flag = true;
        cur[a] = true;
        adj[i].push_back(a);
    }
    if (flag)  {
        cout << "YES";
        return;
    }
    int cnt_cyc = 0;
    for (int i = 1; i <= n; i++) {
        if (!vis[i]) {
            cnt_cyc++;
            dfs(i);
        }
    }
    int ans = n-cnt_cyc;
    cout << (ans%2==0 ? "YES" : "NO");
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
