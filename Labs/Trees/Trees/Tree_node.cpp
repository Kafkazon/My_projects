#include "Tree_node.h"
Tree_node::Tree_node(){
	dat = 0;
	high = 1;
	left = nullptr;
	right = nullptr;
	parent = nullptr;
	left_is_thread = true;
	right_is_thread = true;
};