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
    vector <ll> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    ll ans1, ans2;
    ans1 = a[0];
    ans2 = a[1];
    for (int i = 2; i < n; i+=2) {
        ans1 = __gcd(ans1, a[i]);
    }
    for (int i = 3; i < n; i+=2) {
        ans2 = __gcd(ans2, a[i]);
    }
    bool f1 = true, f2 = true;
    for (int i = 0; i < n; i+=2) {
        if (a[i]%ans2==0) {
            f2 = false;
            break;
        }
    }
    for (int i = 1; i < n; i+=2) {
        if (a[i]%ans1==0) {
            f1 = false;
            break;
        }
    }
    if (f1) {
        cout << ans1;
    }
    else if (f2) {
        cout << ans2;
    }
    else cout << 0;
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
