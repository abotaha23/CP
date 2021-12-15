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

vector <int> adj[200010];

void burn()
{
    int k, n; cin >> n >> k;
    vector <bool> fri(k+1, false);
    while(k--) {
        int i; cin >> i;
        fri[i] = true;
    }
    while(--n) {
        int f, s;
        cin >> f >> s;
        adj[f].push_back(s);
        adj[s].push_back(f);
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
