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
    int n, q, cnt = 0; cin >> n >> q;
    string s; cin >> s;
    for (int i = 0; s[i+2] != '\0'; i++) {
        if (s[i] == 'a' && s[i+1] == 'b' && s[i+2] == 'c') {
            i+=2;
            cnt++;
        }
    }

    while(q--) {
        int pos; char c;
        cin >> pos >> c;
        pos--;
        if (c != s[pos]) {
            if ((c == 'b' && pos > 0 && s[pos-1] == 'a' && pos < s.length()-1 && s[pos+1] == 'c')
                || (c == 'a' && pos < s.length()-2 && s[pos+1] == 'b' && s[pos+2] == 'c')
                || (c == 'c' && pos > 1 && s[pos-1] == 'b' && s[pos-2] == 'a')) cnt++;
            if ((pos < s.length()-2 && s[pos] == 'a' && s[pos+1] == 'b' && s[pos+2] == 'c')
                || (pos > 0 && pos < s.length()-1 && s[pos] == 'b' && s[pos-1] == 'a' && s[pos+1] == 'c')
                || (pos > 1 && s[pos] == 'c' && s[pos-1] == 'b' && s[pos-2] == 'a')) cnt--;
            s[pos] = c;
        }
        cout << cnt << '\n';
    }
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
