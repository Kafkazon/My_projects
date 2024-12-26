#include "Stek.h"

void Stek::push(int nach, int kon) {
	list.insert(0, nach,kon);
}

void Stek::pop() {
	list.del_pos(0);
}

pair<int,int> Stek::get() {
	return list.get_head();
}

void Stek::print() {
	list.print_list();
}

bool Stek::is_empty() {
	return list.is_empty();
}