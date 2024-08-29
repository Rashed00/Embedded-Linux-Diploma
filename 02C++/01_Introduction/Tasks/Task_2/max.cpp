#include <iostream>


int largestElement(int* arr , int size)
{
    int max = arr[0];
    for (int i = 0; i < size; i++)
    {
        if (max < arr[i])
        {
            max = arr[i];
        }   
    }
    return max;
}


int main(int argc, const char** argv) 
{
    int size, temp;
    std::cout << "Enter number of values:" << std::endl;
    std::cin >> size;
    int arr[size];

    std::cout << "Enter values: " << std::endl;
    for (int i = 0; i < size; i++)
    {
        std::cin >> arr[i];
    }
    
    std::cout << "maximum value: "<< largestElement(arr,size) <<std::endl;
    return 0;   
}
        