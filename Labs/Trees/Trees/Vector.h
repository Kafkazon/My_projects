#pragma once
#include <iostream>
#include <stdlib.h>
using namespace std;
class Vector
{
private:
	int* mass;
	int size;
	int end;
	void extend();
public:
	friend ostream& operator << (ostream&, Vector);
	int& operator [] (int);
	bool operator == (Vector);
	Vector();
	void push_back(int elem);
	void print();
	void insert(int ind, int elem);
	void del(int ind);
	int length();
	void copy(Vector vec, int start, int end);
};

