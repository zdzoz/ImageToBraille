#pragma once

#include <string>

class Downloader {
private:
    void* curl;
public:
    Downloader();
    ~Downloader();

    std::string download(const std::string& url);
};
