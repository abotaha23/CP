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
    ll a, b, ans; cin >> a >> b;
    if (a > b) swap(a, b);
    if (b >= 3*a) ans=a;
    else {
        ans=(a+b)/4;
    }
    cout << ans;
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
