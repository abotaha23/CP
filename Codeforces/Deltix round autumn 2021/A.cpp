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

void burn()
{
    ll n, mx = 0; cin >> n;
    ll sum = 0, p = 0;
    while(n--) {
        ll a; cin >> a;
        while(a%2==0) {
            p++;
            a/=2;
        }
        if (mx < a) mx = a;
        sum+=a;
    }
    sum+=mx*(ll)(pow(2, p)-1);
    cout << sum;
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
