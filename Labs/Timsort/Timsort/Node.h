#pragma once
#include <string>
#include <iostream>
using namespace std;
class Node
{
public:
	pair <int,int> id;
	Node* next;
	Node* prev;
	Node();
};