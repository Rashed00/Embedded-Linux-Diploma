#include <iostream>

int main(int argc, const char** argv)
{
    std::cout << "ASCII Code Table:" << std::endl << "+------+-------+" << std::endl << "| Char | ASCII |"<< std::endl << "+------+-------+" << std::endl;
    for(uint8_t i = 32; i < 128; i++)
    {
        std::cout << "|  "<< uint8_t(i) <<"    |   " << uint32_t(i) << "   |"<<std::endl;
    }

    


    
    return 0;
}

