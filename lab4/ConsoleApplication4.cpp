#include <iostream>
#include <vector>
#include <string>
using namespace std;

class BigInt 
{
    vector<int> digits;

public:
    BigInt() {}

    BigInt(const string& num) 
    {
        for (int i = num.length() - 1; i >= 0; --i) 
        {
            digits.push_back(num[i] - '0');
        }
    }

    BigInt(const BigInt& other) : digits(other.digits) {}

    ~BigInt() {}

    BigInt& operator=(const BigInt& other) 
    {
        if (this != &other) 
        {
            digits = other.digits;
        }
        return *this;
    }

    BigInt operator+(const BigInt& other) const 
    {
        BigInt result;
        int carry = 0;
        int len = max(digits.size(), other.digits.size());

        for (int i = 0; i < len || carry; ++i) 
        {
            if (i == result.digits.size()) 
            {
                result.digits.push_back(0);
            }
            result.digits[i] += carry + (i < digits.size() ? digits[i] : 0) + (i < other.digits.size() ? other.digits[i] : 0);
            carry = result.digits[i] / 10;
            result.digits[i] %= 10;
        }

        return result;
    }

    BigInt& operator+=(const BigInt& other) 
    {
        *this = *this + other;
        return *this;
    }

    BigInt operator*(const BigInt& other) const 
    {
        BigInt result;
        result.digits.resize(digits.size() + other.digits.size());

        for (int i = 0; i < digits.size(); ++i) 
        {
            for (int j = 0, carry = 0; j < other.digits.size() || carry; ++j) 
            {
                long long cur = result.digits[i + j] + digits[i] * 1ll * (j < other.digits.size() ? other.digits[j] : 0) + carry;
                result.digits[i + j] = int(cur % 10);
                carry = int(cur / 10);
            }
        }

        while (result.digits.size() > 1 && result.digits.back() == 0) 
        {
            result.digits.pop_back();
        }

        return result;
    }

    BigInt& operator*=(const BigInt& other) 
    {
        *this = *this * other;
        return *this;
    }

    bool operator<(const BigInt& other) const 
    {
        if (digits.size() != other.digits.size()) 
        {
            return digits.size() < other.digits.size();
        }
        for (int i = digits.size() - 1; i >= 0; --i) 
        {
            if (digits[i] != other.digits[i]) 
            {
                return digits[i] < other.digits[i];
            }
        }
        return false;
    }

    bool operator>(const BigInt& other) const 
    {
        return other < *this;
    }

    bool operator==(const BigInt& other) const
    {
        return !(other < *this) && !(*this < other);
    }

    bool operator!=(const BigInt& other) const
    {
        return !(*this == other);
    }

    friend ostream& operator<<(ostream& os, const BigInt& num)
    {
        for (int i = num.digits.size() - 1; i >= 0; --i)
        {
            os << num.digits[i];
        }
        return os;
    }

    friend istream& operator>>(istream& is, BigInt& num)
    {
        string str;
        is >> str;
        num = BigInt(str);
        return is;
    }
};

int main() {
    setlocale(LC_ALL, "RUSSIAN");
    BigInt a("1234567890123456789012345678901234567890");
    cout << "Число a (Оператор <<): " << a << endl;

    BigInt b;
    cout << "Введите число b (Оператор >>): " << b << endl;
    cin >> b;
    cout << "Число b: " << b << endl;

    BigInt sum = a + b;
    cout << "Сумма (Оператор +): " << sum << endl;

    BigInt a2=a;
    a2 += b;
    cout << "Оператор += : " << a2 << endl;

    BigInt product = a * b;
    cout << "Произведение (Оператор *): " << product << endl;

    BigInt a3=a;
    a3 *= b;
    cout << "Оператор *= : " << a3 << endl;

    if (a > b) 
    {
        cout << "Оператор > (a > b)" << endl;
    }
    else if (a < b)
    {
        cout << "Оператор < (a < b)" << endl;
    }
    else if(a==b)
    {
        cout << "Оператор == (a==b)" << endl;
    }
    if (a != b) 
    {
        cout << "Оператор != (a != b)" << endl;
    }
    return 0;
}