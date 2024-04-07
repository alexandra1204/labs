#include <iostream>
#include <vector>

using namespace std;

template <size_t N>
class BitVector 
{
private:
    struct BitField 
    {
        unsigned char bits : 1;
    };

    vector<BitField> data;

public:
    BitVector() : data(N) {}

    void push_back(bool value) 
    {
        data.push_back({ static_cast<unsigned char>(value) });
    }

    bool operator[](size_t index) const 
    {
        if (index >= data.size()) 
        {
            throw out_of_range("index out of range");
        }
        return data[index].bits;
    }
    bool oper(size_t index,bool value) 
    {
        if (index >= data.size()) 
        {
            throw out_of_range("index out of range");
        }
        data[index].bits = value;
        return data[index].bits;
    }

    size_t size() const 
    {
        return data.size();
    }

    void insert(size_t index, bool value) 
    {
        if (index > data.size()) 
        {
            throw out_of_range("index out of range");
        }
        data.insert(data.begin() + index, { static_cast<unsigned char>(value) });
    }

    void erase(size_t index)
    {
        if (index >= data.size()) 
        {
            throw out_of_range("index out of range");
        }
        data.erase(data.begin() + index);
    }
};

int main() {
    setlocale(LC_ALL, "russian");
    BitVector<0> bv;
    
    //Метод добавления в конец вектора
    cout << "Метод добавления в конец вектора и получение по индексу: ";
    bv.push_back(false);
    bv.push_back(true);
    bv.push_back(false);
    for (size_t i = 0; i < bv.size(); ++i)
    {
        cout << bv[i] << " ";
    }
    cout << endl;
    
    //Метод и оператор изменения значения по индексу
    cout << "Изменение значения по индексу: ";
    bv.oper(0, true);
    bv.oper(1, false);
    bv.oper(2, true);
    for (size_t i = 0; i < bv.size(); ++i)
    {
        cout << bv[i] << " ";
    }
    cout << endl;
    
    //	Метод size
    cout << "Size: " << bv.size();
    cout << endl;
    
    //Метод insert
    cout << "insert: " ;
    bv.insert(1, true);
    for (size_t i = 0; i < bv.size(); ++i) 
    {
        cout << bv[i] << " ";
    }
    cout << endl;
    
    //Метод erase
    cout << "erase: ";
    bv.erase(2);
    for (size_t i = 0; i < bv.size(); ++i) 
    {
        cout << bv[i] << " ";
    }
    cout << endl;

    return 0;
}

