#pragma once
#include <string>
#include <iostream>
#include "Tree_node.h"
using namespace std;

class Node
{
public:
	char ch;
	Tree_node* tn;
	Node* next;
	Node* prev;
	Node();
};