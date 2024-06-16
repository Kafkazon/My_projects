#include "AVL_tree.h"

AVL_tree::AVL_tree() {
	head = NULL;
	poisk = NULL;
}
unsigned char height(Tree_node* p)
{	
	if (p != NULL) {
		return p->high;
	}
	return 0;
}

int bfactor(Tree_node* p)
{
	return height(p->right) - height(p->left);
}

void setheight(Tree_node* p)
{
	unsigned char hl = height(p->left);
	unsigned char hr = height(p->right);
	p->high = (hl > hr ? hl : hr) + 1;
}

Tree_node* rotateright(Tree_node* p)
{
	Tree_node* q = p->left;
	p->left = q->right;
	q->right = p;
	setheight(p);
	setheight(q);
	return q;
}

Tree_node* rotateleft(Tree_node* q)
{
	Tree_node* p = q->right;
	q->right = p->left;
	p->left = q;
	setheight(q);	
	setheight(p);
	return p;
}

Tree_node* balance(Tree_node* p)
{
	setheight(p);
	if (bfactor(p) == 2)
	{
		if (bfactor(p->right) < 0)
			p->right = rotateright(p->right);
		return rotateleft(p);
	}
	if (bfactor(p) == -2)
	{
		if (bfactor(p->left) > 0)
			p->left = rotateleft(p->left);
		return rotateright(p);
	}
	return p;
}
void AVL_tree::AVL_construct(Tree_node* trr) {
	if (trr == NULL) {
		return;
	}
	if (head == NULL) {
		head = new Tree_node;
		head->dat = trr->dat;
	}
	else {
		head = insert(head, trr->dat);
	}
	if (trr->left != NULL) {
		AVL_construct(trr->left);
	}
	if (trr->right != NULL) {
		AVL_construct(trr->right);
	}
}

Tree_node* AVL_tree::insert(Tree_node* p, int k) 
{
	if (!p) {
		Tree_node* tn = new Tree_node;
		tn->dat = k;
		return tn;
	}
	if (k < p->dat)
		p->left = insert(p->left, k);
	else
		p->right = insert(p->right, k);
	return balance(p);
}

Tree_node* findmin(Tree_node* p)  
{
	if (p->left) {
		return findmin(p->left);
	}
	return p;
}

Tree_node* removemin(Tree_node* p) 
{
	if (p->left == 0)
		return p->right;
	p->left = removemin(p->left);
	return balance(p);
}
Tree_node* AVL_tree::remove(Tree_node* p, int k) 
{
	if (!p) return 0;
	if (k < p->dat)
		p->left = remove(p->left, k);
	else if (k > p->dat)
		p->right = remove(p->right, k);
	else 
	{
		Tree_node* q = p->left;
		Tree_node* r = p->right;
		delete p;
		if (!r) return q;
		Tree_node* min = findmin(r);
		min->right = removemin(r);
		min->left = q;
		return balance(min);
	}
	return balance(p);
}

void AVL_tree::print(Tree_node* tn,int n) {
	long i;
	if (tn != NULL)
	{
		print(tn->right, n + 5);
		for (i = 0; i < n; i++)
			cout << " ";
		cout << tn->dat << endl;
		print(tn->left, n + 5);
	}
}

Tree_node* AVL_tree::search(Tree_node* tn, int some) {
	if (tn == NULL) {
		return 0;
	}
	if (tn->dat == some) {
		return tn;
	}
	if (some > tn->dat) {
		search(tn->right, some);
	}
	else {
		search(tn->left,some);
	}
}

void AVL_tree::levelOrderPrint(Tree_node* root) {
	if (root == NULL)
	{
		return;
	}
	Queue q;
	q.push(root); 

	while (!q.is_empty()) 
	{
		Tree_node* temp = q.get(); 
		q.pop();  
		cout << temp->dat << " "; 

		if (temp->left != NULL)
			q.push(temp->left);  

		if (temp->right != NULL)
			q.push(temp->right);  
	}
}


void AVL_tree::preorderPrint(Tree_node* root)
{
	if (root == NULL)   
	{
		return;
	}
	std::cout << root->dat << " ";
	preorderPrint(root->left);   
	preorderPrint(root->right);  
}

void AVL_tree::inorderPrint(Tree_node* root)
{
	if (root == NULL)   
	{
		return;
	}
	preorderPrint(root->left);   
	std::cout << root->dat << " ";
	preorderPrint(root->right);  
}

void AVL_tree::postorderPrint(Tree_node* root)
{
	if (root == NULL)   
	{
		return;
	}
	preorderPrint(root->left);   
	preorderPrint(root->right);  
	std::cout << root->dat << " ";
}

void AVL_tree::iterativePreorder(Tree_node* root)
{
	if (root == NULL)
	{
		return;
	}
	Stek_tree s;  
	s.push(root); 
	while (s.is_empty() == false)
	{
		Tree_node* temp = s.get();
		s.pop();
		std::cout << temp->dat << " ";

		if (temp->right)
			s.push(temp->right); 
		if (temp->left)
			s.push(temp->left);  
	}
}
