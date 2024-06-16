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
	void insert(int pos, int id, int size);
	void del_id(double id);
	void del_pos(int pos);
	pair<int, int> get_head();
	pair<int, int> get_ind(int pos);
	void print_list();
	bool is_empty();
};

