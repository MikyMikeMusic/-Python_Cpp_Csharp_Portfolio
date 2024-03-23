#include <iostream>
#include <cstdio>

using namespace std;

class Node {
public:
	int value;
	Node* next;

	Node(int value, Node* next) : value(value), next(next) {}
};

class Stack {
private:
	Node* top_item;
	int max_size;
	int current_size;

public:
	Stack(int max_size) : top_item(nullptr), max_size(max_size), current_size(0) {}

	Node* peek() {
		if (top_item == nullptr) {
			cout << "Stack is empty" << endl;
			return nullptr;
		}
		return top_item;
	}

	void push(int value) {
		if (current_size >= max_size) {
			cout << "Stack is full" << endl;
			return;
		}
		Node* newNode = new Node(value, top_item);
		top_item = newNode;
		current_size++;
	}
	void pop() {
		if (top_item == nullptr) {
			throw underflow_error("Stack is empty");
		}
		Node* temp = top_item;
		top_item = top_item->next;
		delete temp;
		current_size--;
	}

	int top() {
		if (top_item == nullptr) {
			throw underflow_error("Stack is empty");
		}
		return top_item->value;
	}

	int length() {
		int count = 0;
		Node* current = top_item;
		while (current != nullptr)
		{
			count++;
			current = current->next;// Move to the next item
		}
		return count;
	}
};

int main() {
	Stack stack(3);
	for (int i = 0; i <= stack.length(); i++)
	{
		stack.push(i);
		cout << "Pushed to stack: " << i << endl;
	}
	cout << "Top item of the stack: " << stack.top() << endl;
	return 0;

}