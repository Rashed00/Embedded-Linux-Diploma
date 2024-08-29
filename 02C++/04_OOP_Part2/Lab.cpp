#include "iostream"
#include <atomic>
#include <iterator>

class Data
{
public:
    Data(){count++;}
    static int count;
private:
    friend class test;
    int value = 0;
};

int Data::count = 0;

int main(int argc, const char** argv) {
    Data d1;
    Data d2;
    Data d3;
    Data d4;
    std::cout << Data::count << std::endl;
    return 0;
}