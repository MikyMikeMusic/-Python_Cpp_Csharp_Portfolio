#include "Stack.h"

int main()
{
	Stack s(3);

	for (int i = 0; i < s.GetMaxSize(); i++)
	{
		s.push(i);
		cout << s.peek() << endl;	
	}

	return 0;
}