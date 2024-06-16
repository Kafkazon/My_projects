#pragma once
#include "List.h"
class Stek {
private:
	List list;
public:
	void push(int id, int size);
	pair<int, int> get();
	void pop();
	void print();
	bool is_empty();
};