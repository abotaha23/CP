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
    int x, y; cin >> x >> y;
    if((x+y)&1) {
        cout << -1 << ' ' << -1 << endl;
        return;
    }
    for (int i = 0; i < 50; i++) {
        for (int j = 0; j < 50; j++) {
            if ((i+j)*2==x+y && abs(x-i)+abs(y-j)==(x+y)/2) {
                cout << i << ' ' << j << endl;
                return;
            }
        }
    }
}

int main()
{
    Taha_on_da_code;
    int t = 1; cin >> t;
    while(t--) burn();
    return 0;
}
