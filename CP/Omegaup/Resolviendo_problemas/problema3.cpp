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
    int t;
    cin >> t;
    int in1, in2, in3, in4;
    char arr[4] = {'A','B','C','D'};
    REP(0, t) {
        cin >> in1 >> in2 >> in3 >> in4;
        in3 = in1 + in3;
        in4 = in2 + in4;
        REP2(0, 4) {
            cin >> in1 >> in2;
            if (in1 == in3 and in2 == in4) {
                cout << arr[j];
            }
        }
    }
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