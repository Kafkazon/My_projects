#include <iostream>
#include <fstream>
#include "Bin_tree.h"
#include "Queue.h"
#include "AVL_tree.h"
using namespace std;

int main(){
	setlocale(LC_ALL, "RUSSIAN");
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	// Парсинг скобочной последовательности
	string st;
	getline(fin, st);
	Bin_tree bin_tree;
	if (!bin_tree.check_parce(st)) {
		return 0;
	}
	bin_tree.parce(bin_tree.head, st, 0);
	cout << "Парсинг скобочной последовательности:\n";
	//bin_tree.print_good(bin_tree.head,0);
	//cout << "\n\n\n\n\n";
	// Построение АВЛ дерева
	cout << "Построение АВЛ дерева:\n";
	AVL_tree avl_tree;
	avl_tree.AVL_construct(bin_tree.head);
	avl_tree.print(avl_tree.head,0);
	//avl_tree.head = avl_tree.remove(avl_tree.head,10);
	//cout << "\n\n\n\n\n";
	//avl_tree.print(avl_tree.head, 0);

	avl_tree.inorderPrint(avl_tree.head);
	cout << "\n";
	avl_tree.postorderPrint(avl_tree.head);
	cout << "\n";
	avl_tree.preorderPrint(avl_tree.head);
	cout << "\n";
	avl_tree.levelOrderPrint(avl_tree.head);
	cout << "\n";
	fin.close();
	fout.close();
}

