#pragma once
#include "List.h"
class Stek {
private:
	List list;
public:
	void push(char ch);
	char get();
	void pop();
	void print();
	bool is_empty();
};