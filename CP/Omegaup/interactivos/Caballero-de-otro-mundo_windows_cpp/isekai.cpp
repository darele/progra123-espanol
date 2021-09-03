#include "isekai.h"

// Main
//	int battle(int l1, int r1, int l2, int r2)
//	void respuesta(int res)

void encuentraReencarnado(int N) {
	if (N == 1) {
		respuesta(N);
		return;
	}
	int l1, l2, r1, r2, tam, temp;
	l1 = 1;
	for (tam = N / 2; tam >= 1; tam /= 2) {
		r1 = l1 + tam - 1;
		l2 = l1 + tam;
		r2 = r1 + tam;
		temp = battle(l1, r1, l2, r2);
		if (temp == 0) {
			respuesta(r2 + 1);
			return;
		} else if (temp == 1) {
			if (tam == 1) {
				respuesta(l1);
				return;
			}
			continue;
		} else {
			if (tam == 1) {
				respuesta(l2);
				return;
			}
			l1 += tam;
		}
	}

}