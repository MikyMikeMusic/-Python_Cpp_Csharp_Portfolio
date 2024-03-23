#include "Doubly Linked List.h"

using namespace std;

void main()
{
	DoublyLinkedList list;

	// Add some elements to the list
	list.insertHead(1);
	list.insertHead(2);
	list.insertHead(3);
	list.insertAt(1, 4);

	// Test isEmpty on a non-empty 
	list.print();

	// Clear the list
	list.clear();
	cout << "List after clearing: " << list.getSize() << endl;
	cout << "Is Empty: " << list.isEmpty() << endl; // Should print "1	
}