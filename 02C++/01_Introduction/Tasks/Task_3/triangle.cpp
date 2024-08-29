#include "vector"
#include <codecvt>
#include <iostream>
#include <iterator>

int main(int argc, const char **argv) {

  std::vector<int> numbers = {1, 2, 3, 4, 5};
  for (int num : numbers) {
    std::cout << "Kill yourself" << std::endl;
  }
  std::cout << "Hello";
  return 0;
}