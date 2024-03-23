#include "Doubly Linked List.h"

void DoublyLinkedList::insertHead(int data)
{
	Node* newNode = new Node();
	newNode->data = data;

	if (!head)
	{
		head = newNode;
		tail = newNode; // Set tail to newNode since it is the only node in the list
	}
	else
	{
		newNode->next = head; // Set newNode's next pointer to the current head
		head->prev = newNode; // Set the current head's prev pointer to newNode
		head = newNode; // Update head to newNode
	}
	size++;
}

void DoublyLinkedList::insertTail(int data)
{
	Node* newNode = new Node();
	newNode->data = data;

	if (!tail)
	{
		head = newNode; // Set head to newNode since it is the only node in the list
		tail = newNode;
	}
	else
	{
		newNode->prev = tail; // Set newNode's prev pointer to the current tail
		tail->next = newNode; // Set the current tail's next pointer to newNode
		tail = newNode; // Update tail to newNode
	}
	size++;
}

void DoublyLinkedList::print()
{
	Node* current = head;
	while (current)
	{
		std::cout << current->data << " ";
		current = current->next;
	}
	std::cout << std::endl;
}

void DoublyLinkedList::insertAt(int index, int data)
{
	if (index < 0)
	{
		throw std::out_of_range("Invalid index. Index must be greater than or equal to 0.");
	}

	if (index == 0)
	{
		Node* newNode = new Node();
		newNode->data = data;
		newNode->next = head;

		if (head)
		{
			head->prev = newNode;
		}
		else
		{
			tail = newNode;
		}

		head = newNode;
	}
	else if (index >= length())
	{
		// Handle index greater than or equal to the length of the list
		// Insert at the tail
		Node* newNode = new Node();
		newNode->data = data;
		newNode->prev = tail;

		if (tail)
		{
			tail->next = newNode;
		}
		else
		{
			head = newNode;
		}

		tail = newNode;
	}
	else
	{
		// Insert at a specific index
		Node* current = head;
		int currentIndex = 0;

		while (current && currentIndex < index)
		{
			current = current->next;
			currentIndex++;
		}

		Node* newNode = new Node();
		newNode->data = data;
		newNode->prev = current->prev;
		newNode->next = current;

		current->prev->next = newNode;
		current->prev = newNode;
	}
	size++;	
}

void DoublyLinkedList::deleteHead()
{
	if (!head)
	{
		throw std::out_of_range("List is empty.");
	}

	Node* nodeToDelete = head;

	if (head == tail)
	{
		head = nullptr;
		tail = nullptr;
	}
	else
	{
		head = head->next;
		head->prev = nullptr;
	}
	size--;
	delete nodeToDelete;
}

void DoublyLinkedList::deleteTail()
{

	if (!tail)
	{
		throw std::out_of_range("List is empty.");
	}

	Node* nodeToDelete = tail;

	if (head == tail)
	{
		head = nullptr;
		tail = nullptr;
	}
	else
	{
		tail = tail->prev;
		tail->next = nullptr;
	}
	size--;
	delete nodeToDelete;
}

void DoublyLinkedList::deleteAt(int index)
{

	if (index < 0 || index >= length())
	{
		throw std::out_of_range("Invalid index.");
	}

	if (index == 0)
	{
		deleteHead();
	}
	else if (index == length() - 1)
	{
		deleteTail();
	}
	else
	{
		Node* current = head;
		for (int i = 0; i < index; i++)
		{
			current = current->next;
		}

		Node* nodeToDelete = current;
		nodeToDelete->prev->next = nodeToDelete->next;
		nodeToDelete->next->prev = nodeToDelete->prev;

		delete nodeToDelete; 
	}
	size--;
}

int DoublyLinkedList::searchIndex(int data)
{
    Node* current = head;
    int index = 0;
    while (current)
    {
        if (current->data == data)
        {
            return index;
        }
        current = current->next;
        index++;
    }
    return -1; // Return -1 if the data is not found
}

bool DoublyLinkedList::search(int data)
{
	Node* current = head;
	while (current)
	{
		if (current->data == data)
		{
			return true;
		}
		current = current->next;
	}
	return false;
}

void DoublyLinkedList::clear()
{
	while (head)
	{
		Node* nodeToDelete = head;
		head = head->next;
		delete nodeToDelete;
	}
	tail = nullptr;
	size = 0;
}
