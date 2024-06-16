#include "Stek.h"

void Stek::push(char ch) {
	list.insert(0, ch);
}

void Stek::pop() {
	list.del_pos(0);
}

char Stek::get() {
	return list.get_head_char();
}

void Stek::print() {
	list.print_list();
}

bool Stek::is_empty() {
	return list.is_empty();
}