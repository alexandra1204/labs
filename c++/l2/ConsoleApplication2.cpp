
#include <iostream>
using namespace std;
class Matrix 
{
private:
	int rows;
	int cols;
	int** data;

public:

	Matrix(int rows, int cols) : rows(rows), cols(cols) 
    {
		data = new int* [rows];
		for (int i = 0; i < rows; i++) 
        {
			data[i] = new int[cols];
		}
	}

    Matrix(const Matrix& other) : rows(other.rows), cols(other.cols) // конструктор копирования
    {
        data = new int* [rows];
        for (int i = 0; i < rows; i++) 
        {
            data[i] = new int[cols];
            for (int j = 0; j < cols; j++) 
            {
                data[i][j] = other.data[i][j];
            }
        }
    }

    Matrix& operator=(const Matrix& other) // оператор присваивания копированием
    {
        if (&other == this) 
        {
            return *this;
        }

        for (int i = 0; i < rows; i++) 
        {
            delete[] data[i];
        }
        delete[] data;

        rows = other.rows;
        cols = other.cols;
        data = new int* [rows];
        for (int i = 0; i < rows; i++) 
        {
            data[i] = new int[cols];
            for (int j = 0; j < cols; j++) 
            {
                data[i][j] = other.data[i][j];
            }
        }
        return *this;
    }

    ~Matrix() // деструктор
    { 
        for (int i = 0; i < rows; i++) 
        {
            delete[] data[i];
        }
        delete[] data;
    }

    void inputMatrix() 
    {
        for (int i = 0; i < rows; i++)
        {
            for (int j = 0; j < cols; j++) 
            {
                std::cin >> data[i][j];
            }
        }
    }

    void print() 
    {
        for (int i = 0; i < rows; i++) 
        {
            for (int j = 0; j < cols; j++) 
            {
                std::cout << data[i][j] << " ";
            }
            std::cout << std::endl;
        }
    }
};



int main()
{
    setlocale(LC_ALL, "RUSSIAN");
    int n, m;
    cout << "Введите размер матрицы 1 (число строк и столбцов): " << endl;
    cin >> n >> m;
    cout << endl;

    Matrix mat1(n, m);
    mat1.inputMatrix();
    cout << "Матрица 1: " << endl;
    mat1.print();

    Matrix mat2(mat1); // копирование
    cout << "Матрица 2:" << endl;
    mat2.print();

    Matrix mat3(0, 0);
    mat3 = mat1; // присваивание копированием
    cout << "Матрица 3:" << endl;
    mat3.print();

    return 0;
}


