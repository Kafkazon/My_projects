#include <iostream>
#include <fstream>
#include <windows.h>
#include <conio.h>
#include <string>
#include "Vector.h"
#include "Timsort.h"

using namespace std;

int main() {
	setlocale(LC_ALL, "Russian");
	ifstream fin("high.txt");
	ofstream fout("sorted.txt");
	int a;
	bool neg = false;
	Vector vec;
	/*
	cout << "¬ведите массив чисел\n";
	getline(cin, st);
	a = 0;
	for (int i = 0; i < st.length(); i++) {
		if (st[i] != ' ') {
			if (st[i] == '-') {
				neg = true;
				continue;
			}
			a *= 10;
			a += st[i] - '0';
		}
		else {
			if (neg) {
				a *= -1;
				neg = false;
			}
			vec.push_back(a);
			a = 0;
		}
	}
	if (neg) {
		a *= -1;
		neg = false;
	}
	vec.push_back(a);
	vec.print();
	*/
	while (!fin.eof()) {
		fin >> a;
		if (!fin.eof()) {
			vec.push_back(a);
		}
	}
	Timsort tim;
	vec = tim.sort(vec);
	for (int i = 0; i < vec.length(); i++) {
		fout << vec[i] << " ";
	}
	fin.close();
	fout.close();
	return 0;
}