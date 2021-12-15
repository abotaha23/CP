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
    int n, ans = 0, mx = 0; cin >> n;
    vector <int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        if (a[i] > mx) {
            mx = a[i];
        }
    }
    if (mx > a[n-1]) {
        ans++;
        for (int i = n-2; ; i--) {
            if (a[i] > a[n-1]) {
                ans+=(a[i]!=mx);
                for (int j = i, cur = a[i]; a[j] != mx; j--) {
                    if (a[j] > cur) {
                        ans++;
                        cur = a[j];
                    }
                }
                break;
            }
        }
    }
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
