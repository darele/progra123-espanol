//https://omegaup.com/arena/problem/OMI-2020-Primo/#problems

#include "primo.h"
#include <bits/stdc++.h>
#define tam 10000005

using namespace std;

// Main
//	int primo(int posicion)

vector <int> lista;
bitset <tam> p;

void llenar(int n) {
	p.set();
	lista.reserve(100005);
	p[0] = p[1] = 0;
	for (int i = 2; i * i <= n; i++) {
		if (p[i]) {
			for (int j = i * i; j <= n; j += i) {
				p[j] = 0;
			}
		}
	}
	for (int i = 2; i <= n; i++) {
		if (p[i]) {
			lista.push_back(i);
		}
	}
}

int busca(int n) {
	llenar(n);
	int ini, fin, mid;
	ini = 0, fin = lista.size();
	int temp;
	while (fin >= ini) {
		mid = (ini + fin) / 2;
		temp = primo(mid);
		if (lista[mid] == temp) {
			ini = mid + 1;
		} else {
			fin = mid - 1;
		}
	}
	if (temp == lista[mid]) {
		return lista[mid + 1];
	} else {
		return lista[mid];
	}
	return 0;
}