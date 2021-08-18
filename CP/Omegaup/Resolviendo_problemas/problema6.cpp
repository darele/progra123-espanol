#include <bits/stdc++.h>
#define DBG(x) cerr << #x << "=" << (x) << "\n"
#define RAYA cerr << "======================\n"
#define ll long long
#define ii pair <int, int>
#define dl pair <ll, ll>
#define vi vector <int>
#define vl vector <ll>
#define vii vector <ii>
#define graph vector <vi>
#define ff first
#define ss second
#define REP(a, b) for (int i = a; i < b; i++)
#define REP2(a, b) for (int j = a; j < b; j++)
#define REPS(a, b, c) for (int i = a; i < b; i += c)

using namespace std;

int dp[105][105];

void solve() {
    int n;
    cin >> n;
    int in1;
    cin >> in1;
    dp[0][0] = (in1 % 2 == 0);
    for (int i = 1; i < n; i++) {
        cin >> in1;
        dp[i][0] = dp[i - 1][0] + (in1 % 2 == 0);
        for (int j = 1; j < i; j++) {
            cin >> in1;
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + (in1 % 2 == 0);
        }
        cin >> in1;
        dp[i][i] = dp[i - 1][i - 1] + (in1 % 2 == 0);
    }
    int mayor = 0;
    for (int i = 0; i < n; i++) {
        mayor = max(dp[n - 1][i], mayor);
    }
    cout << mayor << "\n";
}

int main() {
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);

    int t = 1;
    //cin >> t;
    while (t--) {
        
        solve();
    }
    return 0;
}