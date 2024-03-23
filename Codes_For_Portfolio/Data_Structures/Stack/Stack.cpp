#include "Stack.h"

void Stack::push(int data)
{
	if (current_size == max_size)
	{
		cout << "Stack is full" << endl;
		return;
	}
	Node* new_node = new Node(data);
	new_node->next = top;
	top = new_node;
	current_size++;
}

void Stack::pop()
{
	if (top == nullptr)
	{
		cout << "Stack is empty" << endl;
		return;
	}
	int data = top->value;
	Node* temp = top;
	top = top->next;
	delete temp;
	current_size--;
}

int Stack::peek()
{
	if (top == nullptr)
	{
		cout << "Stack is empty" << endl;
		return -1;
	}
	return top->value;

}