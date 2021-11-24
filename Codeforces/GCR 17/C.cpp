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
    int n, cnt; cin >> n;
    array <int, 2> p[n];
    for (int i = 0; i < n; i++) {
        cin >> p[i][0] >> p[i][1];
    }
    int st = 0, en = n, m;
    while(st < en) {
        m = (st+en+1)/2; cnt = 0; // this 1 in (st+en+1) is to compensate the
                                // one which we should've added to st = m+1.
        for (int i = 0; i < n; i++) {
            if (p[i][1] >= cnt && p[i][0] >= m-cnt-1) {
                cnt++;
            }
        }
        if (cnt >= m) {
            st = m;
        }
        else {
            en = m-1;
        }
    }
    cout << st << endl;
}

int main()
{
    Taha_on_da_code;
    int t = 1; cin >> t;
    while(t--) burn();
    return 0;
}
