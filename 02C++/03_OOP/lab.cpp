#include "iostream"
#include "string"
#include <codecvt>
#include <iterator>
#include <vector>

class A
{
  public:
  A()
  {
    std::cout << "A" << std::endl;
  }
  ~A()
  {
    std::cout << "~A" << std::endl;
  }
};

class B
{
  public:
  B()
  {
    std::cout << "B" << std::endl;
  }
  ~B()
  {
    std::cout << "~B" << std::endl;
  }
};

class C : A , B
{
  public:
  C()
  {
    std::cout << "C" << std::endl;
  }
  ~C()
  {
    std::cout << "~C" << std::endl;
  }
};

// class LED{    //all methods and members in class are private by default
//   public:
//     unsigned int Number1;
//     unsigned int Number2;
//     void ledTurnOn();   //External function ==> exist in .text  
//     void ledTurnOff()
//     {
//     std::cout << "Led is OFF" << std::endl; //Inline function ==> doesn't exist in .text unless called by instance
//     }
//     LED() = default;     //Default constructor
//     // LED(){std::cout << "Default Constructor" << std::endl;} 
//     LED(int pin);       //Parameter Constructor
    
//   private:
//     int ledPin;
  
// };

// LED::LED(int pin) : ledPin(pin)   //Initializer list
// {
//    // ledPin = pin;   //instead of intialize like this we use intializer list (less assembly instructions)
// }

// void LED::ledTurnOn()
// {
// std::cout << "Led is ON" << std::endl;
// }




// class Data{
//   public:
//     enum class test
//     {
//       HELLO,
//       WORLD
//     };
//     std::string enum_to_string(const test &obj)
//     {
//       switch (obj) {
//         case test::HELLO:
//           return "Hello";
//           case test::WORLD:
//           return "World";
      
//       }
//     }
// };

// struct data {
//   int temp;
// };

// enum class Traffic : unsigned char    //specify size of enum (unlike C style enum had sizeof (int))
// { 
//     RED,
//     GREEN,
//     YELLOW
// };



int main(int argc, const char **argv) {
/*========== Intialization in C++ ===========*/
  // 1-all of them can assign value
  // int x = 10; // Copy Intialization
  // int x2(10); // Direct Intialization
  // int x3{10}; // Value, Uniform Intialization
  // std::cout << x2 << std::endl;
  // std::cout << x3 << std::endl;

  // 2- {} narrow conversion
  // float dec = 3.5;

//   int value{dec}; // conversion must be implicit

  // 3-vexing parse
  // int v{};   //v is intialized with zero 
//   int v2(); // function prototype  ---> int v2(0) will work
  // int v3 = 0;

  // // 4-synthesize constructor
  // int n1;
  // data d1;    /*structure contain garbage values*/
  // data d2{};  /*structure in intialized with zeros*/
  // std::cout << d1.temp << std::endl;
  // std::cout << d2.temp << std::endl;
  // std::cout << n1 << std::endl;

  //constructor(int count, int value)
  // std::vector<int>v1(2,3); //3, 3  -->direct intialization is directing its content to the constructor
  //intializer_list
  // std::vector<int>v2{2,3}; //2, 3    -->Value intialization


  C c;



/*=========== Enum in C++ ===============*/
  // Traffic obj;
  // std::cout << obj <<std::endl;   //cannot print obj till operator overloading exist
  // std::cout << (int)obj <<std::endl;  //to print use casting --static_cast<int>(obj)

  // std::cout << RED << std::cout;   //#error you cannot access literals without class name
  // std::cout << (int)Traffic::RED <<std::endl; //access enum class

  // int ex = Traffic::RED;    //cannot convert from enum to int
  // Traffic::GRsEEN = 1;     //cannot convert int to classic enum

  // int ex = static_cast<int>(Traffic::YELLOW); //conversion happend through casting

  //cannot define function inside enum
  //!workaround: class contain enum and function
  // Data example;
  // std::cout << example.enum_to_string(Data::test::HELLO) << std::endl;

  


  /*========== Class ============*/
  // LED instance;     //Create object in stack
  // instance.ledTurnOn();    //access only public section
  // // instance.ledTurnOff();         +++++
  // // instance.ledPin = 3;   ===>#Error ledPin is private member 
  // std::cout << sizeof(instance) <<std::endl;  //padding + uint8 + uint32 + virtual pointer if exist
  // LED().ledTurnOn();   //Create temporary object just for one line 
  // LED instance(4);
  // std::cout << instance.Number1 << std::endl;
  // std::cout << instance.Number2 << std::endl;






  /*============ Constant ============*/
  //C ==> External linkage
  //C++ ==> Internal linkage

  //constant Switch case 
  // int condition;
  // const int x = 10;
  // switch (condition) {
  // case x:
    // std::cout << "it works" << std::endl;
    // break;
  // default:
    // std::cout << "default" << std::endl;
    // break;
  // }

  //const can be used as array size
  // int arr[x];

  //cannot access const with pointer (unlike C)
  // int* ptr = &x;  //#Error

  //constexpr force the compiler to calculate in compilation time not in run time
  // constexpr int x = rand();  //#Error==>x should be calculated at compilation time

  //Constant functions in classes cannot write on class members
  //it only has access to write on local variables and function parameters
  //ex: 
  // void fun(int temp) const
  // {
      // int x  = 10 ==> valid
      // temp =1 ==> valid
      // classMember = 5 ==>Invalid
  // }

  //Normal instance of class can access (call) both constant function (method) and normal function
  //const instance can only access const const functions (methods)

  //if const method want to access particular member 
  //member shall be defined as mutable
  return 0;

  }