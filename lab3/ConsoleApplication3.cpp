#include <iostream>
using namespace std;
class String 
{
private:
    char* data;
    int length;

public:
    
    String() : data(nullptr), length(0) {}// Базовый конструктор

   
    String(const String& other)  // Конструктор копирования
    {
        length = other.length;
        data = new char[length + 1];
        for (int i = 0; i < length; ++i) 
        {
            data[i] = other.data[i];
        }
        data[length] = '\0';
    }

    

    String& operator=(const String& other) // Оператор присваивания копированием
    {
        if (this != &other) 
        {
            delete[] data;

            length = other.length;
            data = new char[length + 1];
            for (int i = 0; i < length; ++i) 
            {
                data[i] = other.data[i];
            }
            data[length] = '\0';
        }
        return *this;
    }

    String(const char* s)
    {
        length = strlen(s);
        data = new char[length + 1];
        for (int i = 0; i < length; i++) {
            data[i] = s[i];
        }
        data[length] = '\0';
    }
  
    ~String()  // Деструктор
    {
        delete[] data;
    }

   
    String operator+(const String& other)  // Операторы + и +=
    {
        String result;
        result.length = length + other.length;
        result.data = new char[result.length + 1];
        int pos = 0;
        for (int i = 0; i < length; ++i) 
        {
            result.data[pos] = data[i];
            pos++;
        }
        for (int i = 0; i < other.length; ++i) 
        {
            result.data[pos] = other.data[i];
            pos++;
        }
        result.data[result.length] = '\0';
        return result;
    }

    String& operator+=(const String& other) 
    {
        int new_length = length + other.length;
        char* new_data = new char[new_length + 1];
        int pos = 0;
        for (int i = 0; i < length; ++i) 
        {
            new_data[pos] = data[i];
            pos++;
        }
        for (int i = 0; i < other.length; ++i) 
        {
            new_data[pos] = other.data[i];
            pos++;
        }
        new_data[new_length] = '\0';

        delete[] data;
        data = new_data;
        length = new_length;

        return *this;
    }

   
    char& operator[](int index)  // Оператор []
    {
        return data[index];
    }

    
   
    bool operator<(const String& other)  // Операторы <, >, ==
    {
        return strcmp(data, other.data) < 0;
    }

    bool operator>(const String& other) 
    {
        return strcmp(data, other.data) > 0;
    }

    bool operator==(const String& other)
    {
        return strcmp(data, other.data) == 0;
    }

    
    friend ostream& operator<<(ostream& os, const String& str)// Операторы ввода и вывода
    {
        os << str.data;
        return os;
    }

    friend istream& operator>>(istream& is, String& str) 
    {
        char buffer[1000];
        is >> buffer;
        str.length = strlen(buffer);
        str.data = new char[str.length + 1];
        
        for (int i = 0; i < str.length; ++i)
        {
            str.data[i] = buffer[i];
        }
        str.data[str.length] = '\0'; 
        return is;
    }

    
    int find(char c) // Метод find
    {
        for (int i = 0; i < length; ++i)
        {
            if (data[i] == c) 
            {
                return i;
            }
        }
        return -1;
    }


   
    int getLength() // Метод length
    {
        return length;
    }

   
    const char* c_str()  // Метод c_str
    {
        return data;
    }

   
    char& at(int index)  // Метод at
    {
        if (index < 0 || index >= length)
        {
            //throw out_of_range("Index out of range");
            cout << "Index out of range";
        }
        return data[index];
    }
    
    void setAt(int index, char value) 
    {
        if (index < 0 || index >= length)
        {
            throw out_of_range("Index out of range");
        }
        data[index] = value;
    }

    
};

int main()
{
    setlocale(LC_ALL, "Russian");
    String s1;
    cout << "Введите строку 1 (Оператор ввода): " << endl;
    cin >> s1;
    cout << "Строка 1 (Оператор вывода): " << s1 << endl;

    String s2 = s1;
    cout <<"Копирование (строка 2): "<< s2 << endl;
    
    
    String s3("def");
    cout <<"Строка 3: " << s3 << endl;
    s3 = s2;
    cout << "Присваивание копированием (строка 3): " << s3 << endl;

    s3 = s1 + s2;
    cout << "Оператор +: " << s3 << endl;

    s1 += s2;
    cout <<"Оператор +=: "<< s1 << endl;

    cout <<"Оператор [] (чтение): "<< s1[0] << endl;
    s1[0] = 'a';
    cout << "Оператор [] (изменение): " << s1[0] << endl;

    String s4 = "abc";
    cout << "Строка 4: " << s4 << endl;
    if (s4 < s1)
    {
        cout << "Оператор <" << endl;
    }
    if (s4 == s1)
    {
        cout << "Оператор ==" << endl;
    }
    if (s4 > s1)
    {
        cout << "Оператор >" << endl;
    }

    cout <<"Метод find: " << s1.find('f') << endl;

    cout <<"Метод length: "<< s1.getLength() << endl;

    cout <<"Метод c_str:  "<< s1.c_str() << endl;

    cout << "Метод at (получение элемента): " << s1.at(3) << endl;
    String s5;
    s1.setAt(3, 'w');
    cout << "Метод at (изменение): " << s1 << endl;
    cout << "Метод at (выход за пределы): ";
    s1.at(20);

    return 0;
}
