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

vector <vector <int>> adj; vector <bool> fri; vector <int> nf, dis; bool flag;

void dfs1(int cur, int par)
{
    if (cur != 1) dis[cur] = 1+dis[par];
    if (fri[cur]) nf[cur] = 0;
    for (auto &i : adj[cur]) {
        if (i != par) {
            dfs1(i, cur);
            nf[cur] = min(nf[i]+1, nf[cur]);
        }
    }
}

void dfs2(int cur, int par)
{
    if (cur != 1 && adj[cur].size() == 1) {
        flag = true;
        return;
    }
    for (auto &i : adj[cur]) {
        if (i != par && nf[i] > dis[i]) {
            dfs2(i, cur);
        }
    }
}

void burn()
{
    int n, k; cin >> n >> k;
    flag = false;
    fri.assign(n+1, false);
    nf.assign(n+1, 1e9);
    dis.assign(n+1, 0);
    adj.assign(n+1, {});
    for (int i = 0; i < k; i++) {
        int in; cin >> in;
        fri[in] = true;
    }
    for (int i = 1; i < n; i++) {
        int f, s;
        cin >> f >> s;
        adj[f].push_back(s);
        adj[s].push_back(f);
    }
    dfs1(1, 1e9);
    dfs2(1, 1e9);
    cout << (flag ? "YES" : "NO");
}

int main()
{
    Taha_on_da_code;
    int t = 1; cin >> t;
    while(t--) {
        burn();
        cout << '\n';
    }
    return 0;
}
