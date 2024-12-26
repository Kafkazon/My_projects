#include "Queue.h"

Queue::Queue() {
	length = 0;
}

void Queue::push(Tree_node* tn) {
	list.insert(length, tn);
	length++;
}

void Queue::pop() {
	list.del_pos(0);
	length--;
	if (length < 0)
		length = 0;
}

Tree_node* Queue::get() {
	return list.get_head();
}

void Queue::print() {
	list.print_list();
}

bool Queue::is_empty() {
	return list.is_empty();
}