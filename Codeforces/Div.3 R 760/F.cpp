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

string conv(ll n)
{
    string s;
    while(n) {
        s = to_string(n&1)+s;
        n/=2;
    }
    return s;
}

string clr(string s)
{
    string ns;
    int st = 0;
    while(s[st] == '0') st++;
    return s.substr(st, s.length()-st);
}

void burn()
{
    ll x, y; cin >> x >> y;
    if (x==y) {
        cout << "YES";
        return;
    }
    string xs, ys;
    xs = conv(x);
    ys = conv(y);
    queue <string> q;
    q.push(xs);
    set <string> st;
    st.insert(xs);
    while(!q.empty()) {
        string cur = q.front();
        q.pop();
        string cur2 = cur, cur3 = cur+'1';
        reverse(cur2.begin(), cur2.end());
        reverse(cur3.begin(), cur3.end());
        cur2 = clr(cur2);
        if (cur2 == ys || cur3 == ys) {
            cout << "YES";
            return;
        }
        if (cur2.length() < 69 && !st.count(cur2)) {
            st.insert(cur2);
            q.push(cur2);
        }
        if (cur3.length() < 69 && !st.count(cur3)) {
            st.insert(cur3);
            q.push(cur3);
        }
    }
    cout << "NO";
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
