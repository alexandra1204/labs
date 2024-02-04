#include "Header.h"
#include <iostream>
using namespace std;

int main()
{
    setlocale(LC_ALL, "RUSSIAN");
    double l, w;
    cout << "Введите длину и ширину: " << endl;
    cin >> l >> w;

    Rectangle rec(l, w);
    cout << "Площадь: " << rec.area() << endl;
    cout << "Периметр: " << rec.perimeter() << endl;
    cout << "Диагональ: " << rec.diagonal() << endl;
}
