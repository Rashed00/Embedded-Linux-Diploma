#include "iostream"
#include <algorithm>


int main(int argc, const char** argv) {

    unsigned int arr[] = {23, 15 ,1 ,8, 3, 11};
    unsigned int size = sizeof(arr)/sizeof(arr[0]);

    if(std::all_of(arr,arr + size ,[](int i){return i % 2 == 0;}))
    {
        std::cout << "All elemnets are even" << std::endl;
    }
    else
    {
        std::cout << "Array contain at least one odd value" << std::endl;
    }
    
    return 0;
}