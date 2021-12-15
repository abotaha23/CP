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
    int k, n; cin >> n >> k;
    vector <int> disp, disn;
    for (int i = 0; i < n; i++) {
        int in;
        cin >> in;
        in > 0 ? disp.push_back(in) : disn.push_back(-in);
    }
    sort(disn.begin(), disn.end());
    sort(disp.begin(), disp.end());
    ll ans = 0;
    for (int i = disp.size()-1; i >= 0; i-=k) {
        ans+=2*disp[i];
    }
    for (int i = disn.size()-1; i >= 0; i-=k) {
        ans+=2*disn[i];
    }
    if (!disp.empty() && (disn.empty() || !disn.empty() && disp.back() >= disn.back()))
        ans-=disp.back();
    else ans-=disn.back();
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
