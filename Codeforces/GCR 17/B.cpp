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

bool val(vector <int> a, int to_e)
{
    vector <int> b;
    for (auto &i : a) {
        if (i != to_e) {
            b.push_back(i);
        }
    }
    for (int i = 0, j = b.size() - 1; j > i; j--, i++) {
        if (b[i] != b[j]) {
            return false;
        }
    }
    return true;
}

void burn()
{
    int n, k, dis = 0; cin >> n;
    vector <int> a, cur(n+1, 0);
    for (int i = 0; i < n; i++) {
        cin >> k; a.push_back(k);
        if (!cur[a[i]]) dis++;
        cur[a[i]] = 1;
    }
    if (dis < 3) {
        cout << "YES" <<  endl;
        return;
    }
    int to_e1 = 0, to_e2 = 0;
    for (int i = 0, j = n - 1; j > i; j--, i++) {
        if (a[i] != a[j]) {
            to_e1 = a[j];
            to_e2 = a[i];
            break;
        }
    }
    cout << (!to_e1 || val(a, to_e1) || val(a, to_e2) ? "YES" : "NO") << endl;
}
int main()
{
    Taha_on_da_code;
    int t = 1; cin >> t;
    while(t--) burn();
    return 0;
}
