// 408	Uniform Generator

/*
int main()
{
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int n, m;
    while(cin >> n >> m) 
    {
        int s = 0, ans = 1; vector <bool> vis(100000, 0);
        while(ans < m) {s = (s+n)%m; if (vis[s]) break; ans++; vis[s] = 1;}
        cout << setw(10) << n << setw(10) << m << "    ";
        cout << (ans == m ? "Good Choice" : "Bad Choice") << endl << endl;
    }
    return 0;
}

// product

int main()
{
    string x, y;
    while(cin >> x >> y)
    {
        reverse(x.begin(), x.end()); reverse(y.begin(), y.end());
        int ans[500]; memset(ans, 0, sizeof(ans)); 
        for (int i = 0; i < x.length(); i++)
            for (int j = 0; j < y.length(); j++)
                ans[i+j]+=(x[i]-'0')*(y[j]-'0');
        for (int i = 1; i < 500; i++)
            {ans[i]+=ans[i-1]/10; ans[i-1]%=10;}
        int i = 499; while(i > 0 && ans[i] == 0) i--;
        for ( ; i >= 0; i--) cout << ans[i]; cout << endl;
    }
    return 0;
}

// Black and white painting.

int main()
{
    int n, m, c, o, e;
    while(cin >> n >> m >> c)
    {
        e = o = 0;
        if (n == 0 && m == 0 && c == 0) break;
        if (c == 1)
        {
            e = (n-8)/2+1; e*=(m-8)/2+1;
            o = (n-8)/2+(n-8)%2; o*=(m-8)/2+(m-8)%2;
        }
        else
        {
            o = (n-8)/2+1; o*=(m-8)/2+(m-8)%2;
            e = (n-8)/2+(n-8)%2; e*=(m-8)/2+1;
        }
        cout << o+e << endl;

        // a better solution is just :
        cout << ((m-7)*(n-7)+c)/2 << endl;
    }
    return 0;
}

// easy math.

long long lcm(long long a, long long b)
{
    return (a*b)/__gcd(a, b);
}

int main()
{
    long long t, n, m, a, d, ans, k, nums[5]; cin >> t;
    while (t--)
    {
        ans = 0; cin >> n >> m >> a >> d;
        for (int i = 0; i < 5; i++) {nums[i] = a; a+=d;}
        for (int i = 0; i < 5; i++)
        {
            k = nums[i]; ans+=m/k-(n-1)/k;
            for (int i2 = i+1; i2 < 5; i2++)
            {
                k = lcm(nums[i], nums[i2]); ans-=m/k-(n-1)/k;
                for (int i3 = i2+1; i3 < 5; i3++)
                {
                    k = lcm(lcm(nums[i], nums[i2]), nums[i3]); ans+=m/k-(n-1)/k;
                    for (int i4 = i3+1; i4 < 5; i4++)
                    {
                        k = lcm(lcm(nums[i], nums[i2]), lcm(nums[i3], nums[i4])); ans-=m/k-(n-1)/k;
                        for (int i5 = i4+1; i5 < 5; i5++) 
                        {
                            k = lcm(nums[i], lcm(lcm(nums[i2], nums[i3]), lcm(nums[i4], nums[i5])));
                            ans+=m/k-(n-1)/k;
                        }
                    }
                } 
            }
        }
        ans = max((long long) 0, m+1-ans-n);
        cout << ans << endl;
    }
    return 0;
}

// electricity.

bool is_leap(int y)
{
    if (y%100==0) return y%400==0; 
    return y%4==0;
}

int main()
{
    int n, p_d, d; array <int, 4> con[1001];
    while (cin >> n)
    {
        if (!n) break; int cnt = 0, acc = 0;
        for (int i = 0; i < n; i++) cin >> con[i][2] >> con[i][1] >> con[i][0] >> con[i][3];
        for (int i = 1; i < n; i++)
        {
            if (con[i-1][0] == con[i][0])
            {
                if (con[i-1][1] == con[i][1])
                    {if (con[i][2]-con[i-1][2] == 1) {cnt++; acc+=con[i][3]-con[i-1][3];}}
                else if (con[i-1][1]+1 == con[i][1] && con[i][2] == 1)
                {
                    if ((con[i-1][1] == 1 || con[i-1][1] == 3 || con[i-1][1] == 5 || 
                        con[i-1][1] == 7 || con[i-1][1] == 8 || con[i-1][1] == 10 || 
                        con[i-1][1] == 12) && con[i-1][2] == 31) {cnt++; acc+=con[i][3]-con[i-1][3];}
                    else if (con[i-1][1] == 2 && con[i-1][2] == 28+is_leap(con[i-1][0]))
                        {cnt++; acc+=con[i][3]-con[i-1][3];}
                    else if ((con[i-1][1] == 4 || con[i-1][1] == 6 || con[i-1][1] == 9 || 
                        con[i-1][1] == 11) && con[i-1][2] == 30) {cnt++; acc+=con[i][3]-con[i-1][3];}
                }
            }
            else if (con[i-1][0]+1 == con[i][0])
                if (con[i][2] == 1 && con[i][1] == 1 && con[i-1][2] == 31 && con[i-1][1] == 12)
                    {cnt++; acc+=con[i][3]-con[i-1][3];}
        }
        cout << cnt << ' ' << acc << endl;
    }
    return 0;
}
*/