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
    int n, o_n; cin >> n; bool l = 0, f = 0, rf = 0;
    o_n = n;
    while(n) {
        if ((n%10)%2==0) {
            if (n == o_n) f = 1;
            else if (n < 10) l = 1;
            else rf = 1;
        }
        n/=10;
    }
    if (f) cout << 0;
    else if (l) cout << 1;
    else if (rf) cout << 2;
    else cout << -1;
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
