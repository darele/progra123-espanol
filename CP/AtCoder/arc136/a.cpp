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
    //Si econtramos una b solita, si a su derecha hay a, cambiar por bb, y luego por aa
    
    //baa
    //bbba
    //aba
    //abbb
    //aab

    int n;
    cin >> n;
    string s;
    cin >> s;
    string ans;
    for (int i = 0; i < n; i++) {
        if (s[i] == 'B') {
            if (i + 1 < n && s[i + 1] == 'A') {
                ans += 'A';
                s[i + 1] = 'B';
            } else if (i + 1 < n && s[i + 1] == 'B') {
                ans += 'A';
                i++;
            } else {
                ans += 'B';
            }
        } else {
            ans += s[i];
        }
    }
    cout << ans << "\n";
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