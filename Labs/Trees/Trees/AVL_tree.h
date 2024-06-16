#pragma once
#include "Tree_node.h"
#include "Queue.h"
#include "Stek_tree.h"
class AVL_tree
{

public:
	Tree_node* head;
	Tree_node* poisk;
	Tree_node* delitos;
	AVL_tree();
	void AVL_construct(Tree_node* tn);
	Tree_node* insert(Tree_node* tn, int some);
	void print(Tree_node* tn, int n);
	Tree_node* remove(Tree_node* p, int k);
	Tree_node* search(Tree_node* tn, int some);

	void iterativePreorder(Tree_node* root);
	void postorderPrint(Tree_node* root);
	void inorderPrint(Tree_node* root);
	void preorderPrint(Tree_node* root);
	void levelOrderPrint(Tree_node* root);
};

