#pragma once
#include "List.h"
class Queue
{
private:
	int length;
	List list;
public:
	void push(Tree_node* tn);
	Tree_node* get();
	void pop();
	void print();
	bool is_empty();
	Queue();
};

