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
    int n; cin >> n;
    vector <string> a(n-2);
    for (auto &i: a) cin >> i;
    string ans = a[0];
    bool flag = true;
    for (int i = 1; i < n-2; i++) {
        if (flag && a[i-1][1] != a[i][0]) {
            ans+=a[i];
            flag = false;
        }
        else ans+=a[i][1];
    }
    if (ans.length() < n) ans+='a';
    cout << ans;
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
