#include "iostream"
#include "string"
#include <cctype>

int main()
{
    char input;
    std::cin >> input;
    std::cout << isdigit(input) << std::endl;
    return 0;
}