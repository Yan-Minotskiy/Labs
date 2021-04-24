#include <iostream>
using namespace std;
void function()
{
	cout << "Hello world" << endl; 
};

struct stime
{
	int seconds;
	int minutes;
	int hour;
};

class car
{
	private:
		int number;
	public:
		car (int numb): number (numb) {};
		void saynumber(void)
		{
			cout << "Car number is " << number << endl;
		}
};
int main()
{
	void (*pointer)(); //объявление указателя на функцию
	pointer=function; //инициализация указателя на функцию
	pointer(); //вызов функции через указатель
	
	struct stime time1;
	time1.hour=20;
	struct stime *ptr; //объявление указателя на структуру
	ptr=&time1; //инициализация указателя на структуру
	cout << ptr->hour << endl; //получение доступа к элементу указателя, вывод:20
	
	car car1(50);
	car *p=&car1; //инициализация указателя на объект
	p->saynumber(); //доступ к функции объекта
}
/*
Вывод:
Hello world
20
Car number is 50
*/
