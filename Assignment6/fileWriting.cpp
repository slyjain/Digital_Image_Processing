#include <fstream>
#include <iostream>

int main() {
    std::ofstream file("example.bin", std::ios::binary);

    if (!file) {
        std::cerr << "Error opening file!" << std::endl;
        return 1;
    }

    int data = 0x12345678;
    file.write(reinterpret_cast<char*>(&data), sizeof(data));

    char str[] = "Hello, binary world!";
    file.write(str, sizeof(str));

    file.close();

    std::cout << "Data written to example.bin" << std::endl;
    return 0;
}
