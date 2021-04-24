#include <iostream>
using namespace std;
void square(int a) //передача параметра по значению
{
	a=a*a;
	cout << "Into: "<< a << endl;
};
void square2(int *b) //передача параметра по указателю
{
	*b=*b**b;
	cout << "Into: "<< *b << endl;
};
void square3(int &c) //передача параметра по ссылке
{
	c=c*c;
	cout << "Into: "<< c << endl;
};
int main()
{
	int x=5;
	cout << "After: " << x << endl; 
	square(x);
	cout << "Before: " << x << endl;
	x=5;
	cout << "After: " << x << endl;
	square2(&x);
	cout << "Before: " << x << endl;
	x=5;
	cout << "After: " << x << endl;
	square3(x);
	cout << "Before: " << x << endl;
};
/*
Вывод:
After: 5
Into: 25
Before: 5
After: 5
Into: 25
Before: 25
After: 5
Into: 25
Before: 25
*/
