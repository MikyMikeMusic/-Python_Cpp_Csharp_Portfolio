#pragma once
#include <iostream>
#include <string>

class Node {
public: 
	int data;
	Node* next;
	Node* prev;

	Node() : data(0), next(nullptr), prev(nullptr) {} 
};
