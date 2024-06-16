#pragma once
#include "List.h"
class Stek_tree {
private:
	List list;
public:
	void push(Tree_node* tn);
	Tree_node* get();
	void pop();
	void print();
	bool is_empty();
};