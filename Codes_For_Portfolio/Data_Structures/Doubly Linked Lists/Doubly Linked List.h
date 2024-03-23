#pragma once

#include "Node.h"

class DoublyLinkedList {

public:
	Node* head;
	Node* tail;
	int size;

	DoublyLinkedList() : head(nullptr), tail(nullptr), size(0) {}
	~DoublyLinkedList()
	{
		clear();
	}

	void insertHead(int data);
	void insertTail(int data);
	void insertAt(int index, int data);

	void deleteHead();
	void deleteTail();
	void deleteAt(int index);

	int searchIndex(int data);
	bool search(int data);
	
	inline int getSize() const { return size; }
	inline bool isEmpty() const 
	{ 
		if (size == 0)
		{
			return true;
		}
		return false;
	}
	inline int length() 
	{
		int count = 0;
		Node* current = head;

		while (current)
		{
			count++;
			current = current->next;
		}

		return count;
	}
	
	void print();

	void clear();
};
