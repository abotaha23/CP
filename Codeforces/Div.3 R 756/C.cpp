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
    int n, mi = 0; cin >> n;
    vector <int> a(n);
    deque <int> ans;
    for (auto &i : a) {cin >> i; mi = max(mi, i);}
    if (mi != a[0] && mi != a[n-1]) {
        cout << -1;
        return;
    }
    for (int i = 0, j = n-1; j >= i;) {
        if (a[i] >= a[j])
            ans.push_back(a[j--]);
        else
            ans.push_front(a[i++]);
    }
    for (auto &i : ans) {
        cout << i << ' ';
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
