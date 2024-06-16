#include "List.h"
List::List() {
	head = NULL;
	end = NULL;
}
List::~List() {
	if (!is_empty()) {
		poisk = head;
		while (poisk != end) {
			poisk = poisk->next;
			delete poisk->prev;
		}
		delete poisk;
	}
}

void List::insert(int pos, int id, int size) {
	if (head == NULL) {
		head = new Node;
		head->id.first = id;
		head->id.second = size;
		end = head;
		return;
	}
	new_elem = new Node;
	new_elem->id.first = id;
	new_elem->id.second = size;
	int i = 0;
	poisk = head;
	while (i < pos and poisk != NULL) {
		poisk = poisk->next;
		i++;
	}
	if (poisk == NULL) {
		end->next = new_elem;
		new_elem->prev = end;
		end = new_elem;
		return;
	}

	if (poisk == head) {
		head->prev = new_elem;
		new_elem->next = head;
		head = new_elem;
		return;
	}
	new_elem->prev = poisk->prev;
	poisk->prev->next = new_elem;
	new_elem->next = poisk;
	poisk->prev = new_elem;
}

void List::del_id(double id) {
	poisk = head;
	while (poisk != NULL) {
		if (poisk->id.first == id) {
			if (head == end) {
				head = NULL;
				end = head;
				return;
			}
			if (poisk == head) {
				poisk->next->prev = NULL;
				head = poisk->next;
			}
			else
				if (poisk == end) {
					poisk->prev->next = NULL;
					end = poisk->prev;
				}
				else
				{
					poisk->prev->next = poisk->next;
					poisk->next->prev = poisk->prev;
				}
		}
		poisk = poisk->next;
	}
}

void List::del_pos(int pos) {
	int i = 0;
	poisk = head;
	while (poisk != NULL) {
		if (i == pos) {
			if (head == end) {
				head = NULL;
				end = head;
				return;
			}
			if (poisk == head) {
				poisk->next->prev = NULL;
				head = poisk->next;
			}
			else
				if (poisk == end) {
					poisk->prev->next = NULL;
					end = poisk->prev;
				}
				else
				{
					poisk->prev->next = poisk->next;
					poisk->next->prev = poisk->prev;
				}
		}
		poisk = poisk->next;
		i++;
	}
}


pair<int, int> List::get_head() {
	if (head == NULL) {
		return make_pair(0, -1);
	}
	return make_pair(head->id.first, head->id.second);
}

pair<int, int> List::get_ind(int pos) {
	poisk = head;
	int i = 0;
	while (poisk != NULL) {
		if (i == pos) {
			return make_pair(poisk->id.first, poisk->id.second);
		}
		i++;
		poisk = poisk->next;
	}
	cout << "Такого номера нет в списке\n\n";
	return make_pair(0, 0);
}

void List::print_list() {
	poisk = head;
	while (poisk != NULL) {
		cout << poisk->id.first << " " << poisk->id.second << "\n";
		poisk = poisk->next;
	}
}

bool List::is_empty() {
	if (head == NULL)
		return true;
	return false;
}