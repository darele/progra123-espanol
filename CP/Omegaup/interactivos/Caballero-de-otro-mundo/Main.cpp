/*
Hecho por: Progra 123 en espanol
	https://www.youtube.com/channel/UCekalW5zvNJMVgFcenkAECA
link al problema: https://omegaup.com/arena/problem/Caballero-de-otro-mundo/#problems
Link al video donde lo resuelvo: https://youtu.be/1pJdZdJerVk
*/

#include "isekai.h"
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

int N;
int isekai;
int tries = 0;
int exitcode = 1;
int maxTries;

bool validInterval(int l, int r) {
    return (l <= r) and l > 0 and l <= N and r > 0 and r <= N;
}

bool intersect(int u, int l, int r) {
    return (u >= l and u <= r);
}

bool intersect(int l1, int r1, int l2, int r2) {
    return intersect(l1, l2, r2) or intersect(r1, l2, r2) or intersect(l2, l1, r1) or intersect(r2, l1, r1);
}

int battle(int l1, int r1, int l2, int r2) {
    ///Invalid parameters
    if(!validInterval(l1, r1) or !validInterval(l2, r2)) {
        cout << "WA - Los ejercitos no cuentan con intervalos validos." << endl;
        exit(0);
    }
    if(intersect(l1, r1, l2, r2)) {
        cout << "WA - Los equipos se intersectan." << endl;
        exit(0);
    }
    int len1 = r1 - l1 + 1;
    int len2 = r2 - l2 + 1;
    if(tries++ == maxTries) {
        cout << "WA - Maximos intentos excedidos" << endl;
        exit(0);
    }
    if(len1 == len2) {
        if(intersect(isekai, l1, r1)) return 1;
        if(intersect(isekai, l2, r2)) return 2;
        return 0;
    }
    else {
        if(len1 > len2) return 1;
        else return 2;
    }
}

void respuesta(int res) {
    cout << tries << " " << maxTries << endl;
    if(res < 1 or res > N) {
        cout << "WA - Rango de respuesta invalida" << endl;
        exit(0);
    }
    if(res == isekai) {
        cout << "AC" << endl;
        exit(0);
    }
    else {
        cout << "WA - Respuesta incorrecta" << endl;
        exit(0);
    }
}

int main(int argc, char* argv[]) {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cin >> N >> isekai >> maxTries;

	encuentraReencarnado(N);

	cout << "WA - Nunca se llamo la respuesta" << endl;
	return 0;
}
