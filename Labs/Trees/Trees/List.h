#pragma once
#include "Node.h"
class List
{
private:
	pair<int, int> a;
	Node* head;
	Node* end;
	Node* poisk;
	Node* new_elem;
public:
	List();
	~List();
	void insert(int pos, Tree_node* tn);
	void insert(int pos, char tn);
	void del_id(int id);
	void del_pos(int pos);
	Tree_node* get_head();
	char get_head_char();
	//Tree_node get_ind(int pos);
	void print_list();
	bool is_empty();
};

