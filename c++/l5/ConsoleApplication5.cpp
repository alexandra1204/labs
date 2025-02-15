#include <iostream>
using namespace std;

template<class T, int N, int M>
class Matrix 
{

    T data[N][M];

public:
    Matrix() 
    {
        for (int i = 0; i < N; ++i) 
        {
            for (int j = 0; j < M; ++j) 
            {
                data[i][j] = T();
            }
        }
    }

    Matrix(const Matrix& other) 
    {
        for (int i = 0; i < N; ++i)
        {
            for (int j = 0; j < M; ++j) 
            {
                data[i][j] = other.data[i][j];
            }
        }
    }

    Matrix& operator=(const Matrix& other) 
    {
        if (this == &other) 
        {
            return *this;
        }

        for (int i = 0; i < N; ++i)
        {
            for (int j = 0; j < M; ++j) 
            {
                data[i][j] = other.data[i][j];
            }
        }

        return *this;
    }

    Matrix& operator++() 
    {
        for (int i = 0; i < N; ++i)
        {
            for (int j = 0; j < M; ++j) 
            {
                ++data[i][j];
            }
        }
        return *this;
    }

    T& operator()(int i, int j) 
    {
        return data[i][j];
    }

    const T& operator()(int i, int j) const 
    {
        return data[i][j];
    }

    
    

    template<class U, int P, int Q>
    friend Matrix<U, P, Q> operator+(const Matrix<U, P, Q>& m1, const Matrix<U, P, Q>& m2);

    template<class U, int P, int Q>
    friend Matrix<U, P, Q> operator+=(const Matrix<U, P, Q>& m1, const Matrix<U, P, Q>& m2);

    template<class U, int P, int Q>
    friend Matrix<U, P, Q> operator*(const Matrix<U, P, Q>& m, const U& scalar);

    template<class U, int P, int Q>
    friend ostream& operator<<(ostream& os, const Matrix<U, P, Q>& m);

    friend ostream& operator<<(ostream& out, const Matrix<T, N, M>& matrix)
    {
        for (int i = 0; i < N; ++i)
        {
            for (int j = 0; j < M; ++j)
            {
                out << matrix.data[i][j] << " ";
            }
            out << endl;
        }
        return out;
    }

    friend istream& operator>>(istream& in, Matrix<T, N, M>& matrix)
    {
        for (int i = 0; i < N; ++i) 
        {
            for (int j = 0; j < M; ++j)
            {
                in >> matrix.data[i][j];
            }
        }
        return in;
    }
    T det() const
    {
        
        
        static_assert(N == M, "N!=M");
        
        
        if (M == N == 1)
        {
            return data[0][0];
        }
        else if (M == N == 2) 
        {
            return data[0][0] * data[1][1] - data[0][1] * data[1][0];
            
        }
        else if (M == N == 3) 
        {
            return data[0][0] * data[1][1] * data[2][2] + data[1][0] * data[2][1] * data[0][2] + data[0][1] * data[1][2] * data[2][0] - data[0][2] * data[1][1] * data[2][0] - data[0][1] * data[1][0] * data[2][2] - data[0][0] * data[1][2] * data[2][1];
            
        }
        
        

    }
};

template<class T, int N, int M>
Matrix<T, N, M> operator+(const Matrix<T, N, M>& m1, const Matrix<T, N, M>& m2) 
{
    Matrix<T, N, M> result;

    for (int i = 0; i < N; ++i) 
    {
        for (int j = 0; j < M; ++j)
        {
            result(i, j) = m1(i, j) + m2(i, j);
        }
    }

    return result;
}

template<class T, int N, int M>
void operator+=(Matrix<T, N, M>& m1, const Matrix<T, N, M>& m2)
{
    for (int i = 0; i < N; ++i) 
    {
        for (int j = 0; j < M; ++j)
        {
            m1(i, j) += m2(i, j);
        }
    }
}

template<class T, int N, int M>
Matrix<T, N, M> operator*(const Matrix<T, N, M>& m, const T& scalar)
{
    Matrix<T, N, M> result;

    for (int i = 0; i < N; ++i) 
    {
        for (int j = 0; j < M; ++j) 
        {
            result(i, j) = m(i, j) * scalar;
        }
    }

    return result;
}

template<class T, int N, int M>
void operator*=(Matrix<T, N, M>& m, const T& scalar) 
{
    for (int i = 0; i < N; ++i)
    {
        for (int j = 0; j < M; ++j) 
        {
            m(i, j) *= scalar;
        }
    }
}

int main() 
{
    setlocale(LC_ALL, "RUSSIAN");
    
    
    cout << "Введите элементы матрицы 1 размером 3х3:" << endl;
    Matrix<int,3, 3> M1;
    cin >> M1;


    cout << "Введите элементы матрицы 2 размером 3х3:" << endl;
    Matrix<int, 3, 3> M2;
    cin >> M2;


    cout << "Матрица 1:" << endl << M1 << endl;
    cout << "Матрица 2:" << endl << M2 << endl;


    Matrix<int, 3, 3> M3 = M1 + M2;
    cout << "Матрица 3 (оператор +):" << endl << M3 << endl;
    M1 += M2;
    cout << "оператор +=:" << endl <<M1<<  endl;


    Matrix<int, 3, 3> M4 = M1 * 2;
    cout << "оператор *:" << endl << M4 << endl;
    M1 *= 2;
    cout << "оператор *=:" << endl << M1 << endl;


    ++M1;
    cout << "оператор ++:" << endl << M1 << endl;

    
    cout <<"Определитель: " << M1.det()<<endl<<endl;


    M1(1, 1) = 99;
    cout<<"Замена элемента матрицы по индексу: " <<endl<< M1;
    
    
    return 0;
}
