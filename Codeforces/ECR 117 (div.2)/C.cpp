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

void burn()
{
    ll k, x, cnt = 0; cin >> k >> x;
    if (x >= k*k) {
        cnt = 2*k-1;
    }
    else if (x > (k+1)*k/2) {
        cnt=2*k-1;
        x = k*k-x;
        cnt-=ll(floor((sqrt(8*x+1)-1)/2));
    }
    else {
        cnt=ll(ceil((sqrt(8*x+1)-1)/2));
    }
    cout << cnt << endl;
}

int main()
{
    Taha_on_da_code; // solved after the contest but no problem as you got it my lil boy
    int t = 1; cin >> t;
    while(t--) burn();
    return 0;
}

