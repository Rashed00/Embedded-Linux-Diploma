#include "iostream"
#include <codecvt>
#include <string>
#include <utility>
// void function(int y, int x = 2) { std::cout << x + y << std::endl; }

void test(int a, int b) { std::cout << a + b << std::endl; }

void test(double a, int b) { std::cout << a + b << std::endl; }

int main(int argc, const char **argv) {

  // std::cout << "Hello World!" << std::endl;
  // function(3);
  // test(3, 0);
  // test(3.9, 1);

  // int arr[5] = {1, 3, 4, 5, 9};


  // for (int value : arr) {
  //   value += 1;
  //   std::cout << value << std::endl;
  // }

  // int x = 10;
  // int &y = x;
  // std::cout << y << " " << x << std::endl;
  
//   auto var = 10;
//   auto var1 = 10.3;
//   auto var2 = 'a';
//   const int x = 1;
//   auto var3 = x;
//   const auto var4 = x;
//   auto &y = x;

//   auto lst = {1.5,0.0,3.1,4.1,9.36,5.8};
//   auto var5 = std::string("Hello string");  
// // 
//   int a = 97;
//   char b = 'a';

//   int* q = (int*) &b;
//   std::cout << static_cast<int>(b) << std::endl;
  return 0;
}