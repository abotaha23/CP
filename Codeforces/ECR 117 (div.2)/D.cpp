#include <iostream>
#include <bits/stdc++.h>
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

//const int d4i[4]={-1, 0, 1, 0}, d4j[4]={0, 1, 0, -1};
//const int d8i[8]={-1, -1, 0, 1, 1, 1, 0, -1}, d8j[8]={0, 1, 1, 1, 0, -1, -1, -1};

void burn()
{
    ll a, b, x, lim;
    cin >> a >> b >> x;
    while(a) {
        if (x%a == b%a && x >= a && x <= b) {
            // x must be between a && b (inclusive) as we can
            // just take the difference between them
            cout << "YES" << endl;
            return;
        }
        b%=a; swap(a, b);
    }
    cout << "NO" << endl;
}

int main()
{
    Taha_on_da_code;
    int t = 1; cin >> t;
    while(t--) burn();
    return 0;
}

