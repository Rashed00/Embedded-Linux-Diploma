#include "iostream"
#include <atomic>
#include <csignal>

void signal_callback_handler(int signum) {
   std::cout << "Caught signal " << signum << std::endl;
   // Terminate program
   exit(signum);
}
int main(){
   // Register signal and signal handler
   std::signal(SIGINT, signal_callback_handler);
   while(true){
      std::cout << "Program processing..." << std::endl;
      sleep(1);
   }
   return 0;
}