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

void burn()
{
    ll n, s, ans = -1, i = 0, j = 0, st, en;
    cin >> n >> s; vector <int> a(n);
    for (auto &e : a) cin >> e;
    while(j < n) {
        s+=a[j++];
        while(i < j && s < 0) {
            s-=a[i++];
        }
        if (ans < j-i && j != i) {
            ans = j-i;
            st = i+1;
            en = j;
        }
    }
    if (ans < 0) cout << -1;
    else cout << st << ' ' << en;
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
