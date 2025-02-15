#include <iostream>
#include <fstream>
#include <memory>
#include <vector>

class DataReader {
protected:
    std::ifstream m_in;
    std::string m_filename;
    uint8_t m_n;
public:
    DataReader(const std::string& filename) : m_filename(filename), m_n(0) {}
    virtual ~DataReader() {}

    virtual bool Open() = 0;
    void Close() {
        m_in.close();
    }
    virtual void Read() = 0;
    virtual void Write() = 0;
    virtual void GetData(std::vector<uint8_t>& buf, uint8_t& n) = 0;
};

class TxtReader : public DataReader {
private:
    std::unique_ptr<uint8_t[]> m_data;
public:
    TxtReader(const std::string& filename) : DataReader(filename), m_data(nullptr) {}

    bool Open() override {
        m_in.open(m_filename);
        return m_in.is_open();
    }

    void Read() override {
        int tmp;
        m_in >> tmp;
        m_n = tmp;
        m_data = std::make_unique<uint8_t[]>(m_n);
        for (int i = 0; i < m_n; i++) {
            int tmp;
            m_in >> tmp;
            m_data[i] = tmp;
        }
    }

    void Write() override {}

    void GetData(std::vector<uint8_t>& buf, uint8_t& n) override {
        n = m_n;
        buf.resize(m_n);
        for (int i = 0; i < m_n; i++)
            buf[i] = m_data[i];
    }
};

class BinReader : public DataReader {
private:
    std::unique_ptr<uint8_t[]> m_data;
public:
    BinReader(const std::string& filename) : DataReader(filename), m_data(nullptr) {}

    bool Open() override {
        m_in.open(m_filename, std::ios::binary);
        return m_in.is_open();
    }

    void Read() override {
        m_in.read((char*)&m_n, 1);
        m_data = std::make_unique<uint8_t[]>(m_n);
        m_in.read((char*)m_data.get(), m_n);
    }
    

    void Write() override {}

    void GetData(std::vector<uint8_t>& buf, uint8_t& n) override {
        n = m_n;
        buf.resize(m_n);
        for (int i = 0; i < m_n; i++)
            buf[i] = m_data[i];
    }
    
};
class BinFReader : public DataReader 
{
private:
    std::unique_ptr<float[]> m_data;
public:
    BinFReader(const std::string& filename) : DataReader(filename), m_data(nullptr) {}

    bool Open() override 
    {
        m_in.open(m_filename, std::ios::binary);
        return m_in.is_open();
    }

    void Read() override
    {
        m_in.read((char*)&m_n, sizeof(unsigned int));
        m_data = std::make_unique<float[]>(m_n);
        m_in.read((char*)m_data.get(), m_n * sizeof(float));
    }

    void Write() override {}

    void GetData(std::vector<uint8_t>& buf, uint8_t& n) override
    {
        n = m_n;
        buf.resize(n * sizeof(float) + sizeof(unsigned int));
        std::memcpy(buf.data(), &m_n, sizeof(unsigned int));
        std::memcpy(buf.data() + sizeof(unsigned int), m_data.get(), n * sizeof(float));
    }
};

DataReader* Factory(const std::string& filename) {
    std::string extension = filename.substr(filename.find_last_of('.') + 1);
    if (extension == "txt")
        return new TxtReader(filename);
    else if (extension == "bin")
        return new BinReader(filename);
    else if (extension == "binf")
        return new BinFReader(filename);
    return nullptr;
}

int main() {
    std::vector<uint8_t> buf;
    uint8_t n;


    std::cout << "input1.txt"<< std::endl;
    std::unique_ptr<DataReader> Reader(Factory("input1.txt"));
    if (!Reader)
        return -1;

    if (!Reader->Open())
        return -1;

    Reader->Read();
    Reader->GetData(buf, n);

    std::cout << static_cast<int>(n) << std::endl;
    for (int i = 0; i < n; i++)
        std::cout << static_cast<int>(buf[i]) << std::endl;
    


    std::cout << "input2.bin"<< std::endl;
    std::unique_ptr<DataReader> Reader2(Factory("input2.bin"));
    
    if (!Reader2)
        return -1;

    if (!Reader2->Open())
        return -1;

    Reader2->Read();
    Reader2->GetData(buf, n);

    std::cout << static_cast<int>(n) << std::endl;
    for (int i = 0; i < n; i++)
        std::cout << static_cast<int>(buf[i]) << std::endl;



    std::cout << "input3.binf" << std::endl;
    std::unique_ptr<DataReader> Reader3(Factory("input3.binf"));

    if (!Reader3)
        return -1;

    if (!Reader3->Open())
        return -1;

    Reader3->Read();
    Reader3->GetData(buf, n);

    std::cout << static_cast<float>(n) << std::endl;
    for (int i = 0; i < n; i++)
        std::cout << static_cast<float>(buf[i+1]) << std::endl;

    return 0;
}
