#pragma once


class Rectangle {
	double length;
	double width;
public:
	Rectangle(double l, double w);
	~Rectangle();
	double area();
	double perimeter();
	double diagonal();

};