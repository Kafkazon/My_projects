#include "Vector.h"

Vector::Vector() {
	mass = (int*)calloc(2, sizeof(int));
	size = 2;
	end = 0;
}

void Vector::extend() {
	size *= 2;
	mass = (int*)realloc(mass, size * sizeof(int));
}

void Vector::push_back(int elem) {
	if (end >= size - 1) {
		extend();
	}
	mass[end] = elem;
	end++;
}

void Vector::print() {
	for (int i = 0; i < end; i++) {
		cout << mass[i] << " ";
	}
	cout << endl;
}

void Vector::insert(int ind, int elem) {
	if (ind < end) {
		for (int i = end; i >= ind; i--) {
			mass[i + 1] = mass[i];
		}
		mass[ind] = elem;
		end++;
	}
	else
		if (ind == end) {
			push_back(elem);
		}
		else
			cout << "Incorrect position\n";
};

int &Vector::operator[] (int id) {
	return mass[id];
}
bool Vector::operator == (Vector b) {
	if (end != b.length()) {
		return false;
	}
	for (int i = 0; i < end; i++) {
		if (mass[i] != b[i]) {
			return false;
		}
	}
	return true;
}

ostream& operator << (ostream& os, Vector a) {
	os << a.mass;
	return os;
}

void Vector::del(int ind) {
	for (int i = ind; i < end; i++) {
		mass[i] = mass[i + 1];
	}
	end--;
}

int Vector::length() {
	return end;
}

void Vector::copy(Vector vec, int start, int end) {
	for (int i = start; i < end; i++) {
		push_back(vec[i]);
	}
}