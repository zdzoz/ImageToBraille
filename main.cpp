#include <iostream>
#include "Downloader.h"
#include <string>

using namespace std;
//
int main(int argc, char *argv[]){

    Downloader downloader;
    std::string content = downloader.download("https://stackoverflow.com");
    std::cout << content << std::endl;

}
