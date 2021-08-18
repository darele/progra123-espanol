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

void solve() {
    int n, x;
    cin >> n >> x;
    int arr[n];
    REP(0, n) {
        cin >> arr[i];
    }
    REP(x, n) {
        if (arr[i] != arr[x]) {
            cout << "Imposible\n";
            return;
        }
    }
    int ans = 0;
    for (int i = x - 1; i >= 0; i--) {
        //cout << "algo" << endl;
        if (arr[i] != arr[x]) {
            ans = i + 1;
            break;
        }
    }
    cout << ans<< "\n";
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