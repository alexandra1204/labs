#include "Header.h"
#include <cmath>
Rectangle::Rectangle(double l, double w) : length(l), width(w) {}

Rectangle::~Rectangle() {}

double Rectangle::area()
{
	return length * width;
}
double Rectangle::perimeter() 
{
	return 2 * (length + width);
}

double Rectangle::diagonal() 
{
	return sqrt(length * length + width * width);
}
