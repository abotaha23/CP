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

//const int di[8]={0, 0, 1, -1, 1, -1, -1, 1}, dj[8]={1, -1, 0, 0, 1, -1, 1, -1};
map <int, vector <int>> adj;  int pos[200010]; bool flag;
void dfs(int cur)
{
    for (auto &i : adj[cur]) {
        if (pos[i] > pos[cur]) {
            dfs(i);
        }
        else {
            flag = false;
            return;
        }
    }
}

void burn()
{
    int n, b, r; cin >> n; flag = true;
    adj.clear(); vector <int> ans(n+1, 0),
    p(n+1), par(n+1), dis(n+1, 0);
    for (int i = 1; i <= n; i++) {
        cin >> b;
        if (b != i) {
            adj[b].push_back(i);
            par[i] = b;
        }
        else r = b;
    }
    for (int i = 1; i <= n; i++) {
        cin >> p[i];
        pos[p[i]] = i;
    }
    dfs(r);
    if (!flag || p[1] != r) {
        cout << -1;
        return;
    }
    for (int i = 2; i <= n; i++) {
        ans[p[i]] = dis[p[i-1]]+1-dis[par[p[i]]];
        dis[p[i]] = dis[p[i-1]]+1;
    }
    for (int i = 1; i <= n; i++) {
        cout << ans[i] << ' ';
    }
}

int main()
{
    Taha_on_da_code;
    int t = 1;  cin >> t;
    while(t--) {
        burn();
        cout << endl;
    }
    return 0;
}
