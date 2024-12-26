#include "Stek_tree.h"

void Stek_tree::push(Tree_node* tn) {
	list.insert(0, tn);
}

void Stek_tree::pop() {
	list.del_pos(0);
}

Tree_node* Stek_tree::get() {
	return list.get_head();
}

void Stek_tree::print() {
	list.print_list();
}

bool Stek_tree::is_empty() {
	return list.is_empty();
}