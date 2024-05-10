#include <iostream>
#include <vector>
using namespace std;

template<size_t N>
class BitVector 
{
    vector<unsigned char> data;
    size_t size_;

public:
    BitVector() : data((N + 7) / 8, 0), size_(0) {}

    void push_back(bool value)
    {
        if (size_ >= N) 
        {
            throw out_of_range("BitVector is full");
        }
        size_t byte_index = size_ / 8;
        size_t bit_index = size_ % 8;
        if (value)
        {
            data[byte_index] |= (1 << bit_index);
        }
        else 
        {
            data[byte_index] &= ~(1 << bit_index);
        }
        ++size_;
    }

    bool operator[](size_t index) const
    {
        if (index >= size_)
        {
            throw out_of_range("Index out of range");
        }
        size_t byte_index = index / 8;
        size_t bit_index = index % 8;
        return (data[byte_index] >> bit_index) & 1;
    }

    bool operator[](size_t index) 
    {
        if (index >= size_)
        {
            throw out_of_range("Index out of range");
        }
        size_t byte_index = index / 8;
        size_t bit_index = index % 8;
        return (data[byte_index] >> bit_index) & 1;
    }

    void set(size_t index, bool value) 
    {
        if (index >= size_) 
        {
            throw out_of_range("Index out of range");
        }
        size_t byte_index = index / 8;
        size_t bit_index = index % 8;
        if (value) 
        {
            data[byte_index] |= (1 << bit_index);
        }
        else 
        {
            data[byte_index] &= ~(1 << bit_index);
        }
    }

    size_t size() const 
    {
        return size_;
    }
    void insert(size_t index, bool value) 
    {
        if (index > size_)
        {
            throw out_of_range("Index out of range");
        }
        if (size_ >= N) {
            throw out_of_range("BitVector is full");
        }
        data.push_back(0);
        ++size_;
        for (size_t i = size_ - 1; i > index; --i) 
        {
            set(i, operator[](i - 1));
        }
        set(index, value);
    }

    void erase(size_t index)
    {
        if (index >= size_)
        {
            throw out_of_range("Index out of range");
        }
        for (size_t i = index; i < size_ - 1; ++i) 
        {
            set(i, operator[](i + 1));
        }
        --size_;
        data.pop_back();
    }
};

int main() {
    setlocale(LC_ALL, "russian");
    BitVector<10> bv;
    
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
    
    //Метод изменения значения по индексу
    cout << "Изменение значения по индексу: ";
    bv.set(0, true);
    bv.set(1, false);
    bv.set(2, true);
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
