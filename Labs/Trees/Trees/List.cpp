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

void List::insert(int pos, Tree_node* tn) {
	if (head == NULL) {
		head = new Node;
		head->tn = tn;
		end = head;
		return;
	}
	new_elem = new Node;
	new_elem->tn = tn;
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

void List::insert(int pos, char ch) {
	if (head == NULL) {
		head = new Node;
		head->ch = ch;
		end = head;
		return;
	}
	new_elem = new Node;
	new_elem->ch = ch;
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

void List::del_id(int id) {
	poisk = head;
	while (poisk != NULL) {
		if (poisk->tn->dat == id) {
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

char List::get_head_char() {
	if (head == NULL) {
		return 0;
	}
	return head->ch;
}

Tree_node* List::get_head() {
	if (head == NULL) {
		return 0;
	}
	return head->tn;
}

/*
Tree_node* List::get_ind(int pos) {
	poisk = head;
	int i = 0;
	while (poisk != NULL) {
		if (i == pos) {
			return poisk->tn;
		}
		i++;
		poisk = poisk->next;
	}
	cout << "Такого номера нет в списке\n\n";
	return head->tn;
}
*/
void List::print_list() {
	poisk = head;
	while (poisk != NULL) {
		cout << poisk->tn->dat << " ";
		poisk = poisk->next;
	}
	cout << "\n";
}

bool List::is_empty() {
	if (head == NULL)
		return true;
	return false;
}