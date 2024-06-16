#pragma once
#include <iostream>
#include "Tree_node.h"
#include "Queue.h"
#include "Stek.h"
using namespace std;

class Bin_tree
{
public:
	Tree_node* node;
	Tree_node* head;
	Queue q;
	bool otr;
	void parce(Tree_node* tn, string st, int n);
	bool check_parce(string& st);
	void add_node(int a);
	void print(Tree_node* tn);
	void print_good(Tree_node* tn, int n);
	Tree_node* find_bfs(Tree_node* tn);
	Tree_node* get_head();
	Bin_tree();
};

