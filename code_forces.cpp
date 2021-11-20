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
#include <map>
#include <queue>
 
typedef long long ll;
#define Taha_on_da_code ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

using namespace std;

/*

// A4-watermelon

int main()
{
    int w; bool flag = true;
    do
    {
        cin >> w;
    } while((w < 1 || w > 100));
    for (int i = 2; i < w; i+=2)
        if ((w - i) % 2 == 0)
        {
            cout << "YES" << endl;
            flag = false;
            break;
        } 
    
    if (flag) cout << "NO" << endl;
    return 0;
}


//A-Pizzaforces


long long int less_time(long long int);


int main()
{
    int t; long long int n;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        cin >> n;
        cout << less_time(n) << endl;
    }
    return 0;
}

long long int less_time(long long int n)
{
    int pizzas[] = {6, 8, 10}, times[] = {15, 20, 25};
    for (int i = 0; i < 3; i++)
        if (n % pizzas[i] == 0) return (n/pizzas[i])*times[i];
    for (int i = 0; ;i++)
    {
        for (int j = 0; j < 3; j++)
            if ((n+i)%pizzas[j] == 0 && n+i >= pizzas[j])
                return (n+i)/pizzas[j]*times[j];
        for (int j = 0; j < 3; j++)
            for (int l = 0; l < 3; l++)
                if ((n+i-pizzas[j])%pizzas[l] == 0 && (n+i-pizzas[j]) >= pizzas[l])
                    return (n+i-pizzas[j])/pizzas[l] * times[l] + times[j];
    }
}


// A-cherry

int main()
{
    int t, n, counter = 0;
    cin >> t;
    for (int l = 0; l < t; l++)
    {
        long long int max_prod = 0;
        cin >> n;
        counter += n;
        if (counter > 300000) break;
        long long int* nums = new long long int[n];
        for (int i = 0; i < n; i++)
            cin >> nums[i];
        for (int i = 0; i < n-1; i++)
        {
            if (max_prod < nums[i]*nums[i+1])
                max_prod = nums[i]*nums[i+1];
        }
        cout << max_prod << endl;
    }
    return 0;
}


// coin rows (still uncompleted)

int main()
{
    int t, m, total = 0, bob_score,;
    cin >> t;
    for (int i = 0; i < t && total < 100000; i++)
    {   
        bob_score = 0;
        cin >> m;
        total += m;
        int* matrix = new int[2*m];
        for (int j = 0; j < 2*m;j++)
            cin >> matrix[j];
        matrix[0] = 0; matrix[2*m-1] = 0;
        for (int j = 1; j < m; j++)
        {
            int sum_up = 0, sum_down = 0;
            if (matrix[j] < matrix[j+m]) matrix[j] = 0;
            else
            {
                for (int n = j; n < m; n++) sum_up += matrix[j]; // j+1 cuz we don't count j.
                for (int n = j+m-1; n < 2*m-1; n++) sum_down += matrix[n];
                if (sum_up > sum_down)
                {
                    for (int n = j+m; n < 2*m-1; n++)
                        matrix[n] = 0;
                    break;
                }
            }
        }
        for (int j = 1; j < m-2; j++)
        {
            if (matrix[j] > matrix[j+m]) bob_score += matrix[j];
            else
            {
                for (int n = j; n < 2*m-1; n++) sum_up += matrix[j];
                for (int n = j+m; n < 2*m-1; n++) sum_down += matrix[n];
                if (sum_up < sum_down)
                {
                    bob_score += sum_down;
                    break;
                }
                else
            }
        }

        cout << bob_score << endl;   
    }
    return 0;
}


// dislike of threes

bool liked(int);

int main()
{
    int t, k;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        cin >> k;
        int num = 1, n = 1;
        while (n < k || !(liked(num)))
            if (liked(num++)) n++;
        cout << num << endl;
    }
    return 0;
}

bool liked(int num)
{
    if (num % 3 != 0 && num % 10 != 3)
        return 1;
    return 0;
}


// B. who's opposite

int main() 
{
  int t, nums[3], Min, Max;
  cin >> t;
  for (int i = 0; i < t; i++)
  {
    for (int j = 0; j < 3; j++) cin >> nums[j];
    if (nums[0] < nums[1]) 
    {
      Min = nums[0];
      Max = nums[1];
    }
    else
    {
      Min = nums[1];
      Max = nums[0];
    }
    if (Max < 2*Min || nums[2] > 2*(Max - Min))
      cout << -1 << endl;
    else if (nums[2] > Max)
      cout << nums[2] - Max + Min << endl;
    else if (nums[2] > Min)
    {
      if (Max - Min < nums[2])
        cout << nums[2] - Max + Min << endl;
      else
        cout << nums[2] + Max - Min << endl;
    }
    else
      cout << nums[2] + Max - Min << endl;
  }
  return 0;
}


// c.infinity table

int main()
{
    int t;
    long int k;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        cin >> k;
        for (int n = 0; ; n++)
        {
            if (sqrt(k-n) == int(sqrt(k-n)))
            {
                if (n == 0)
                {
                    cout << int(sqrt(k)) << " " << 1 << endl;
                    break;
                }
                else if (n <= sqrt(k-n) + 1)
                {
                    cout << n << " " << int(sqrt(k-n)) + 1 << endl;
                    break;
                }
                else
                {
                    cout << int(sqrt(k-n)) + 1 << " " << 2*(int(sqrt(k-n)) + 1) - n << endl;
                    break;
                }
            }
        }
    }
    return 0;
}


// A. Domino Disaster

int main()
{
    int t, n; string s;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        cin >> n;
        cin >> s;
        for (int j = 0; j < n; j++)
        {
            if (s[j] == 'U') s[j] = 'D';
            else if (s[j] == 'D') s[j] = 'U';
        }
        cout << s << endl;
    }
    return 0;
}


// B. scenes from the memory (incompleted)

const int LIMIT = 10;
 
int main()
{   
    stringstream conv;
    int t, k, n, temp, len; string s, e; bool found;
    int not_primes[LIMIT], i = 1;
    not_primes[0] = 1;
    for (int n = 4; i < LIMIT; n++)
    {
        for (int j = 2; j <= int(sqrt(n)); j++)
            if (n % j == 0)
            {
                not_primes[i++] = n;
                break;
            }
    }
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        found = true;
        cin >> k;
        cin >> s;
        for (int j = 0; j < LIMIT && found; j++)
        {
            len = 0;
            temp = not_primes[j];
            while (temp != 0)
            {
                len++;
                temp/=10;
            }
            conv << not_primes[j]; conv >> e;
            for (int n = 0; n < len; n++)
            {    
                found = false;
                for (int m = 0; m < k; m++)
                    if (s[m]-'0' == e[n]-'0')
                    {
                        found = true;
                        break;
                    }
                if (!(found)) break;
            }
            if (found)
            {
                cout << len << endl << e << endl;
            }
        }
    }
    return 0;
}


// A. the miracle and the sleeper

int main()
{
    int t, r, l;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        cin >> l; cin >> r;
        if (r/2+1 > l)
            cout << r%(r/2+1) << endl;
        else
            cout << r % l << endl; 
    }
    return 0;
}


// A. Simply Strange Sort (incomleted)

int main()
{
    int t, n;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        cin >> n;
        int* nums = new int[n];
        for (int j = 0; j < n; < j++)
            cin >> nums[j];
        
    }
}


// B. Mocha and Red and Blue


// countdown
int main()
{   
    int t, n, n_operations; string s;
    cin >> t;
    while(t--)
    {
        n_operations = 0;
        cin >> n >> s;
        for (int i = 0; i < n; i++)
        {
            if (s[i] != '0')
                if (i != n-1)
                    n_operations += s[i] - '0' + 1;
                else
                    n_operations += s[i] - '0';
        }
        cout << n_operations << endl;
    }
    return 0;
}


// swap (false)

int main()
{
    int t, n, minimum; bool flag;
    cin >> t;
    while(t--)
    {
        minimum = INT_MIN;
        flag = true;
        cin >> n;
        int* a = new int[n];
        int* b = new int[n];
        for (int j = 0; j < n; j++)
            cin >> a[j];
        for (int l = 0; l < n; l++)
            cin >> b[l];
        for (int i = 0; i < n && (flag || i < minimum); i++)
            for (int j = i; j < n && (flag || j+i < minimum); j++)
            {
                if(a[j] < b[i] || b[j] > a[i])
                {
                    minimum = i+j;
                    flag = false;
                }
            }
        cout << minimum << endl;
    }
    return 0;
}


// min MEX cut

int main()
{
    int t, NO_ones, NO_zeros, l; string s;
    cin >> t;
    while(t--)
    {   
        NO_ones = NO_zeros = 0;
        cin >> s;
        for (l = 0; s[l] != '\0'; ) l++;
        for (int i = 0; i < l; i++)
        {
            if (s[i] == '0') 
            {
                NO_zeros++;
                while(s[i+1] == '0')
                    i++;
            }
            else NO_ones++;
        }
        if (NO_zeros == 0) cout << 0 << endl;
        else if (NO_ones == 0 || NO_zeros == 1) cout << 1 << endl;
        else cout << 2 << endl;   
    }
    return 0;
}


// Educational Codeforces Round 114 (div 2) (my first contest)

// A.regular bracket sequance

int main()
{
    int t, n, j, k, len, limit, a_j;
    cin >> t;
    while(t--)
    {
        cin >> n;
        for (int i = 0; i < n; i++)
        {
            len = 2*n; a_j = 0;
            do
            {
                limit = n-i;
                if (n < 2*a_j) limit = n-a_j;
                for (j = 0; j < limit; j++)
                    cout << '(';
                for (k = 0; k < limit; k++)
                    cout << ')';
                len -= 2*j;
                a_j += j;
            } while (len);
            cout << endl;
        }
    }
    return 0;
}



// A.digit sum

int main()
{
    int t, n, count; cin >> t;
    while(t--)
    {
        cin >> n; count = 0;
        if (n%10 == 9) count++;
        if (n > 9) count += n/10;
        cout << count << endl;
    }
    return 0;
}


// B. swaps (wrong)
int main()
{
    int t, nums[3], m, count;
    cin >> t;
    while(t--)
    {
        count = 0; flag = true;
        cin >> nums[0] >> nums[1] >> nums[2] >> m;
        sort(nums, nums + 3);
        for(int i = 0; i < 3; i++) count += nums[i]/2;
        if ((nums[2]-nums[1]-nums[0])/2 > m || count < m)
            cout << "no" << endl;
        else cout << "yes" << endl;
    }
    return 0;
}


//A. boy or girl


int main()
{
    speed_up;
    string name; int i, count = 0;
    cin >> name;
    for (i = 0; name[i] != '\0'; i++)
        for (int j = i+1; name[j] != '\0'; j++)
            if (name[i] != '0' && name[i] == name[j]) 
            {
                count--;
                name[j] = '0';
            }
    count += i;
    if (count%2) cout << "IGNORE HIM!" << endl;
    else cout <<  "CHAT WITH HER!" << endl;
    return 0;
}

int main()
{
    speed_up;
    int t, n, k; string v_s; char s[40];
    cin >> t;
    while (t--)
    {
        cin >> n; k = 0;
        cin >> s; v_s = s;
        sort(s, s+n);
        for (int i = 0; i < n; i++)
            if (s[i] != v_s[i]) k++;
        cout << k << endl;
    }
    return 0;
}


// A.Arrival of the general

int main()
{
    speed_up;
    int n, h, max_h, min_h, max_i, min_i, num_op = 0;
    min_h = min_i = INT_MAX; max_h = max_i = INT_MIN;
    cin >> n;
    for (int i = 0; i < n; i++) 
    {
        cin >> h;
        if (h > max_h) {max_h = h; max_i = i;}
        if(h <= min_h) {min_h = h; min_i = i;} // here I added the equal sign cuz I need it to be as near as possible to the end.
    }
    num_op += max_i+(n-min_i-1);
    if (min_i < max_i) num_op--;
    cout << num_op << endl;
    return 0;
}

// A.Bit++

int main()
{
    speed_up;
    int n, x = 0; string s;
    cin >> n;
    while(n--)
    {
        cin >> s;
        if (s.substr(1, 3) == "++" || s.substr(0, 2) == "++") x++;
        else x--;
    }
    cout << x << endl;
    return 0;
}

int main()
{
    speed_up;
    int n, t_m, a[100000], p[100000]; 
    cin >> n; t_m = 0;
    for (int i = 0; i < n; i++) cin >> a[i] >> p[i];
    t_m += a[0]*p[0];
    for (int i = 1; i < n; i++)
    {
        if (p[i-1] < p[i]) p[i] = p[i-1];
        t_m += p[i] * a[i];
    }
    cout << t_m << endl;
    return 0;
}

// B.duff in love

int main()
{
    speed_up;
    long long n, p, divisors[100000]; bool flag;
    cin >> n; p = 0;
    for (long long i = 1; i <= sqrt(n); i++)
        if (n%i==0) {divisors[p++] = i; divisors[p++] = n/i;}
    sort(divisors, divisors + p+1);
    for (long long i = p; i >= 0; i--)
    {   
        flag = true;
        for (long long j = 2; j*j <= divisors[i]; j++)
            if (divisors[i] % (j*j) == 0) {flag = false; break;}
        if (flag) {cout << divisors[i]; break;}
    }
    return 0;
}

// a better solution using vectors

int main()
{
    speed_up;
    long long n; bool flag;
    vector<long long> divisors;
    cin >> n;
    for (long long i = 1; i <= sqrt(n); i++)
        if (n%i==0) {divisors.push_back(i); divisors.push_back(n/i);}
    sort(divisors.begin(), divisors.end());
    for (long long i = divisors.size()-1; i >= 0; i--)
    {   
        flag = true;
        for (long long j = 2; j*j <= divisors[i]; j++)
            if (divisors[i] % (j*j) == 0) {flag = false; break;}
        if (flag) {cout << divisors[i]; break;}
    }
    return 0;
}
 // A.polycarb and coins
int main()
{
    speed_up;
    int t, n, c1; cin >> t;
    while(t--)
    {
        cin >> n;
        c1 = n/3;
        if (n%3 == 1) c1++;
        cout << c1 << " " << (n-c1)/2 << endl;
    }
    return 0;
}

// B1.wonderful coloring

int main()
{
    speed_up;
    string s; int t, n, d_n, cur; cin >> t;
    while(t--)
    {
        cin >> s; d_n = 0;
        for (n = 0; s[n] != '\0'; n++)
        {
            cur = 0;
            for (int i = n+1; s[i] != '\0' && s[n] != '0'; i++)
                if (s[n] == s[i]) {cur++; s[i] = '0';}
            if (cur > 1) d_n+=(cur-1);
        }
        cout << (n-d_n)/2 << endl;
    }
    return 0;
}

// A. find the array

int main()
{
    speed_up;
    int t, s, count, d;
    cin >> t;
    while(t--)
    {
        cin >> s; count = 0; d = 1;
        while (s)
        {
            s -= d; count++; d += 2;
            while (s-d < 0) d--;
        }
        cout << count << endl;
    }
    return 0;
}

// A.Compote

int main()
{
    speed_up;
    int a, b, c, count = 0;
    cin >> a >> b >> c;
    while (!count && a)
    {
        if (a <= c/4 && a <= b/2) count = 7*a;
        else a--;
    }
    cout << count << endl;
    return 0;
}

// B.Decoding

int main()
{
    speed_up;
    int n, i = 0; string s, r_s = ""; cin >> n >> s;
    while(i < n-1)
    {
        if (n%2)
        {
            if (i % 2) r_s = s[i++] + r_s;
            else r_s = r_s + s[i++]; 
        }
        else
        {
            if (i % 2) r_s = r_s + s[i++];
            else r_s = s[i++] + r_s; 
        }
    }
    r_s += s[i];
    cout << r_s << endl;
    return 0;
}

// C.ticks (incompleted)

int main()
{
    speed_up;
    int t, n, m, k, r, l, dum_k, dum_r, dum_l; string s; bool flag; cin >> t;
    while(t--)
    {
        cin >> n >> m >> k >> s; flag = true;
        for (int i = n*m-1; i >= 0; i--)
        {
            s[i] = '.'; r = l = i; dum_k = k; dum_l = l; dum_r = r;
            while ((dum_r-n+1)/m == 1 + dum_r/m && dum_r-n-1 >= 0 && dum_l-n-1 >= 0 && (dum_l-n-1)/m == 1 + dum_l/m) {dum_k--; dum_l-=(n+1); dum_r-=(n+1);}
            if (!dum_k)
                while ((r-n+1)/m == 1 + r/m && r-n+1 >= 0 && l-n-1 >= 0 && (l-n-1)/m == 1 + l/m)
                {
                    r -= (n-1); l -= (n+1);
                    s[r] = '.'; s[l] = '.';
                }
        }
        for (int i = 0; i < n*m; i++) if (s[i] != '.' || dum_k) {cout << "no" << endl; flag = false; break;}
        if (flag) cout << "yes" << endl;
    }
    return 0;
}



// B.Moamen and k-subsequences (incompleted)
int main()
{
    speed_up;
    int t, n, k, dum_n, nums[100000]; bool flag;
    cin >> t;
    while (t--)
    {
        flag = true;
        cin >> n >> k;
        dum_n = n;
        for (int j = 0; j < n; j++) cin >> nums[j];
        if (n == k) { cout << "yes\n"; continue; }
        for (int i = 0; i < n-1; i++)
        {
            if (nums[i] < nums[i+1])
            {
                dum_n--;
                for (int l = 0; nums[i+1]-nums[i] != 1 && l < n; l++)
                    if (nums[i] < nums[l] < nums[i+1]) { dum_n++; break; }
            }
            if (k == dum_n) { cout << "yes\n"; flag = false; break; }
        }
        if (flag) cout << "no\n";
    }
    return 0;
}

// Two Buttons
int main()
{
    Taha_on_da_code;
    int n, m, dis[20010]; cin >> n >> m;
    memset(dis, 0, sizeof dis);
    if (n >= m) {cout << n-m; return 0;} queue <int> bfs;
    bfs.push(n);
    while(!bfs.empty()) {
        int cur = bfs.front();
        bfs.pop();
        if (cur == m) {
            cout << dis[cur];
            return 0;
        }
        for (int i = 0; i < 2; i++) {
            int d = (i%2 ? 2*cur : cur-1);
            if (d < 2*m && d > 0 && !dis[d]) {
                dis[d] = dis[cur] + 1;
                bfs.push(d);
            }
        }
    }
    return 0;
}

// Kefa and Park

vector <int> adj[100010];
int obs[100010];
 
void dfs(int cur, int m, int p, int c, int m_c, int &cnt)
{
    int ch = 0;
    if (obs[cur]) c++;
    else c = 0;
    m_c = max(c, m_c);
    for (auto &i : adj[cur]) {
        if (i != p) {
            dfs(i, m, cur, c, m_c, cnt);
            ch++;
        }
    }
    if (!ch && m_c <= m) cnt++;
}
 
int main()
{
    Taha_on_da_code;
    int n, m, cnt = 0, p = 0; cin >> n >> m;
    for (int i = 1; i <= n; i++) {
        cin >> obs[i];
    }
    while(--n) {
        int f, t; cin >> f >> t;
        adj[f].push_back(t);
        adj[t].push_back(f);
    } dfs(1, m, p, 0, 0, cnt);
    cout << cnt;
    return 0;
}

// Learning Languages

vector <int> adj[101]; set <int> nodes;
 
void dfs(int cur)
{
    nodes.erase(cur);
    if (nodes.empty()) return;
    for (auto &i : adj[cur])
        if (nodes.find(i) != nodes.end()) dfs(i);
}
 
int main()
{
    Taha_on_da_code;
    int n, m, k, l, cost = 0; bool flag = false; cin >> n >> m;
    while(n--) {
        int c; cin >> c;
        if (!c) cost++;
        else {
            cin >> k;
            nodes.insert(k);
            while (--c) {
                cin >> l;
                adj[k].push_back(l);
                adj[l].push_back(k);
                nodes.insert(l);
            }
        }
    }
    while (!nodes.empty()) {
        cost++; flag = true;
        dfs(*nodes.begin());
    }
    cout << cost-flag;
    return 0;
}

// Reposts

map <string, vector<string>> pu;
map <string, bool> vis; int c = 0, l_c = 0;
 
void dfs(string cur)
{
    c++; l_c = max(l_c, c);
    vis[cur] = true;
    for (auto &i : pu[cur]) {
        if (!vis[i]) dfs(i);
        c--;
    }
}
 
int main()
{
    Taha_on_da_code;
    int n; string f, g, t; cin >> n;
    while(n--) {
        cin >> t >> g >> f;
        for (auto &i : f) i = tolower(i);
        for (auto &i : t) i = tolower(i);
        pu[f].push_back(t);
    } dfs("polycarp");
    cout << l_c;
    return 0;
}

// DZY loves chemistry
 
vector <int> adj[3000]; set <int> nodes;
 
void dfs(int cur, int &l)
{
    nodes.erase(cur);
    for (auto &i : adj[cur]) {
        if (nodes.find(i) != nodes.end()) {
            l++; dfs(i, l);
        }
    }
}
 
int main()
{
    Taha_on_da_code;
    int n, m, l; ll ans = 1; cin >> n >> m;
    while(m--) {
        int f, t; cin >> f >> t;
        adj[f].push_back(t);
        adj[t].push_back(f);
        nodes.insert(f);
        nodes.insert(t);
    }
    while(!nodes.empty()) {
        l = 1;
        dfs(*nodes.begin(), l);
        ans*=(ll)pow(2, l-1);
    }
    cout << ans;
    return 0;
}


// Mr. Kitayuta's Colorful Graph

vector <int> adj[101][101]; set <int> col; bool vis[101];
 
void dfs (int c, int x, int y, int &cnt)
{
    vis[x] = true;
    if (x == y) {cnt++; return;}
    for (auto &i : adj[c][x]) {
        if (!vis[i]) dfs(c, i, y, cnt);
    }
}
 
int main()
{
    Taha_on_da_code;
    int n, m; cin >> n >> m;
    while(m--) {
        int a, b, c;
        cin >> a >> b >> c;
        col.insert(c);
        adj[c][a].push_back(b);
        adj[c][b].push_back(a);
    }
    int q; cin >> q;
    while(q--) {
        int x, y, cnt = 0; cin >> x >> y;
        for (auto &i : col) {
            memset(vis, false, sizeof vis);
            dfs(i, x, y, cnt);
        }
        cout << cnt << endl;
    }
    return 0;
}

// Choosing Capital for Treeland

map <int, vector <pair <int, int>>> adj; map <int, int> ans; bool vis[200001]; set <int> nodes;

void dfs(int cur)
{
    vis[cur] = true;
    for (auto &i : adj[cur]) {
        if (!vis[i.first]) {
            ans[i.first] = ans[cur] + i.second;
            dfs(i.first);
        }
    }
}

void ginit(int cur)
{
    vis[cur] = true;
    for (auto &i : adj[cur]) {
        if (!vis[i.first]) {
            if (i.second < 0) ++ans[1];
            ginit(i.first);
        }
    }
}

int main()
{
    Taha_on_da_code;
    int n; cin >> n;
    for (int i = 1; i < n; i++) {
        int f, t; cin >> f >> t;
        nodes.insert(f); nodes.insert(t);
        adj[f].emplace_back(t, 1);
        adj[t].emplace_back(f, -1);
    }
    memset(vis, 0, sizeof vis);
    ginit(1);
    memset(vis, 0, sizeof vis);
    dfs(1);
    int m = n;
    for (auto &i : nodes) {
        m = min(ans[i], m);
    }
    vector <int> anss;
    for (auto &i : nodes) {
        if (ans[i] == m) {
            anss.push_back(i);
        }
    }
    cout << m <<  endl;
    for (auto &i : anss) cout << i << ' ';
    return 0;
}

// Ice Cave

string g[501]; int dx[] = {-1, 1, 0, 0}, dy[] = {0, 0, -1, 1};
 
void dfs(int x, int y, int &xw, int &yw, int &n, int &m, bool &ans)
{
    g[y][x] = 'X';
    for (int i = 0; i < 4; i++) {
        if (x+dx[i] >= 0 && x+dx[i] < m && y+dy[i] >= 0 && y+dy[i] < n) {
            if (yw == y+dy[i] && xw == x+dx[i]) {ans = true; return;}
            if (g[y+dy[i]][x+dx[i]] == '.')
                dfs(x + dx[i], y + dy[i], xw, yw, n, m, ans);
        }
    }
}
 
int main()
{
    Taha_on_da_code;
    int n, m, x0, y0, x, y, cnt = 0; bool ans = false; cin >> n >> m;
    for (int i = 0; i < n; i++) cin >> g[i];
    cin >> y0 >> x0 >> y >> x; x0--; y0--; x--; y--;
    for (int i = 0; i < 4; i++) {
        if (x+dx[i] >= 0 && x+dx[i] < m && y+dy[i] >= 0 && y+dy[i] < n) {
            if (g[y+dy[i]][x+dx[i]] == '.' || (x0 == x+dx[i] && y0 == y+dy[i])) cnt++;
        }
    }
    dfs(x0, y0, x, y, n, m, ans);
    cout << (ans && (g[y][x] == 'X' || cnt > 1) ? "YES" : "NO");
    return 0;
}

// Permutation Transformation

string g[501]; int dx[] = {-1, 1, 0, 0}, dy[] = {0, 0, -1, 1};
 
void dfs(int x, int y, int &xw, int &yw, int &n, int &m, bool &ans)
{
    g[y][x] = 'X';
    for (int i = 0; i < 4; i++) {
        if (x+dx[i] >= 0 && x+dx[i] < m && y+dy[i] >= 0 && y+dy[i] < n) {
            if (yw == y+dy[i] && xw == x+dx[i]) {ans = true; return;}
            if (g[y+dy[i]][x+dx[i]] == '.')
                dfs(x + dx[i], y + dy[i], xw, yw, n, m, ans);
        }
    }
}
 
int main()
{
    Taha_on_da_code;
    int n, m, x0, y0, x, y, cnt = 0; bool ans = false; cin >> n >> m;
    for (int i = 0; i < n; i++) cin >> g[i];
    cin >> y0 >> x0 >> y >> x; x0--; y0--; x--; y--;
    for (int i = 0; i < 4; i++) {
        if (x+dx[i] >= 0 && x+dx[i] < m && y+dy[i] >= 0 && y+dy[i] < n) {
            if (g[y+dy[i]][x+dx[i]] == '.' || (x0 == x+dx[i] && y0 == y+dy[i])) cnt++;
        }
    }
    dfs(x0, y0, x, y, n, m, ans);
    cout << (ans && (g[y][x] == 'X' || cnt > 1) ? "YES" : "NO");
    return 0;
}

// Books Exchange (hard version)

vector <int> adj[200010], done; bool vis[200010];
 
void dfs(int cur, int it, int &inc)
{
    done.push_back(cur-1);
    vis[cur] = true;
    for (auto &i : adj[cur]) {
        if (!vis[i]) dfs(i, it+1, inc);
        else {inc = it; return;}
    }
}
 
void burn()
{
    int n, inc = 1; cin >> n; vector <int> a(n), ans(n);
    memset(vis, 0, sizeof vis);
    for (int i = 1, p; i <= n; i++) {
        cin >> p;
        adj[i].push_back(p);
    }
    for (int i = 1; i <= n; i++) {
        if (!vis[i]) {
            dfs(i, 1, inc);
            for (auto &j: done) {
                ans[j] = inc;
            }
            done.clear();
        }
    }
    for (auto &i : ans) cout << i << ' ';
    cout << endl;
    for (int i = 1; i <= n; i++) adj[i].clear();
}
 
int main()
{
    Taha_on_da_code;
    int t; cin >> t;
    while(t--) burn();
    return 0;
}

// Fox And Two Dots

string a[51]; bool vis[51][51];
int dx[] = {0, 0, 1, -1}, dy[] = {1, -1, 0, 0};
 
void dfs (int y, int x, bool & ans, int it, char c, int m, int n, int x0, int y0)
{
    vis[y][x] = true; it++;
    for (int i = 0; i < 4; i++) {
        if (x+dx[i] >= 0 && x+dx[i] < m && y+dy[i] >= 0 && y+dy[i] < n) {
            if (a[y+dy[i]][x+dx[i]] == c) {
                if (x+dx[i] == x0 && y+dy[i] == y0 && it >= 4) {ans = true; return;}
                if (!vis[y+dy[i]][x+dx[i]])
                    dfs(y+dy[i], x+dx[i], ans, it, c, m, n, x0, y0);
            }
        }
    }
}
 
int main()
{
    Taha_on_da_code;
    int n, m; cin >> n >> m; bool ans = false;
    for (int i = 0; i < n; i++) cin >> a[i];
    for (int i = 0; !ans && i < n; i++) {
        for (int j = 0; !ans && j < m; j++) {
            memset(vis, 0, sizeof vis);
            dfs(i, j, ans, 0, a[i][j], m, n, j, i);
        }
    }
    cout << (ans ? "Yes" : "No");
    return 0;
}

// Secret Passwords

vector <int> adj[200100]; map <int, bool> vis;
 
void dfs (int cur)
{
    vis[cur] = true;
    for (auto &i : adj[cur]) {
        if (!vis[i]) dfs(i);
    }
}
 
int main()
{
    Taha_on_da_code;
    int n, ans = 0; string s; cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> s;
        for (auto &j: s) {
            adj[i].push_back(n+j-'a');
            adj[n+j-'a'].push_back(i);
        }
    }
    for (int i = n; i < n+26; i++) {
        if (!adj[i].empty() && !vis[i]) {
            ans++; dfs(i);
        }
    }
    cout << ans;
    return 0;
}

*/
