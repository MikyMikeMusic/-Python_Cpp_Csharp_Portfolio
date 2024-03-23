#pragma once
#include "Node.h"

class Stack
{
private:
	Node* top;
	int max_size;
	int current_size;

public:
	Stack(int max_size) : top(nullptr), max_size(max_size), current_size(0) {}

	inline int GetCurrentSize()
	{
		return current_size;
	}
	inline int GetMaxSize()
	{
		return max_size;
	}

	void push(int data);
	void pop();
	int peek();

	inline bool isEmpty() { return top == nullptr; }
	inline bool isFull() const { return current_size == max_size; }

};
