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
#define tam 5005

using namespace std;

void mover(int a[], int i) {
    swap(a[i], a[i + 2]);
    swap(a[i + 1], a[i + 2]);
}

bool iguales(int a[], int b[], int n) {
    for (int i = 0; i < n; i++) {
        if (a[i] != b[i]) {
            return false;
        }
    }
    return true;
}

bool bublesort(int a[], int n, int b[]) {
    for (int i = n - 1; i >= 0; i--) {
        //Soy el unico que siente que esto no va a salir bien?
        int j;
        for (j = 0; j < i - 2; j++) {
            if (a[j] == b[i]) {
                mover(a, j);
            }
        }
        if (a[j] == b[i]) {
            mover(a, j - 1);
            j++;
        }
        if (iguales(a, b, n)) {
            return true;
        }
    }
    if (iguales(a, b, n)) {
        return true;
    }
    return false;
}

void solve() {
    int n;
    cin >> n;
    int a[n];
    int b[n];
    int rep1[tam];
    int rep2[tam];
    for (int i = 0; i < tam; i++) {
        rep1[i] = rep2[i] = 0;
    }
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        rep1[a[i]]++;
    }
    for (int i = 0; i < n; i++) {
        cin >> b[i];
        rep2[b[i]]++;
    }
    for (int i = 0; i < tam; i++) {
        if (rep1[i] != rep2[i]) {
            cout << "No\n";
            return;
        }
    }
    cout << (bublesort(a, n, b) ? "Yes" : "No") << "\n";

    //La vida es bella, hagamolo en O(n^2)
    //paso1: verificar las repeticiones de cada numero
    //listo
    //paso2: Hacer el bubblesort pero con el shift que hemos visto, es decir,
    //      mover siempre el elemento de la derecha de b hacia la derecha en a.
    //      por ahora trabajemos en esa funcion
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