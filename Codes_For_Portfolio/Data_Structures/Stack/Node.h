#pragma once

#include <iostream>
#include <string>

using namespace std;

class Node
{
public:
	int value;
	Node* next;

	Node(int value) : value(value), next(nullptr) {}

};


