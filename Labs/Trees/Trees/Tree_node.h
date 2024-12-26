#pragma once
#include <iostream>

using namespace std;
class Tree_node
{
public:
	Tree_node();
	int dat;
	int high;
	Tree_node* left, * right, *parent;
	bool left_is_thread, right_is_thread;
	
};

