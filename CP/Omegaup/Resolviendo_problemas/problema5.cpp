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

int n, m;
ll arr[50][50];
ll suma[100];

void solve() {
    arr[0][0] = 1;
    arr[1][0] = 1;
    arr[1][1] = 1;
    suma[0] = 1;
    suma[1] = 3;
    for (int i = 2; i <= 40; i++) {
        arr[i][0] = 1;
        arr[i][i] = 1;
        suma[i] = suma[i - 1] + 2;
        for (int j = 1; j < i; j++) {
            arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j];
            suma[i] += arr[i][j];
        }
    }
}

int main() {
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);

    int t = 1;
    cin >> t;
    solve();
    while (t--) {
        cin >> n >> m;
        cout << suma[m] - suma[n - 1] << "\n";
    }
    return 0;
}