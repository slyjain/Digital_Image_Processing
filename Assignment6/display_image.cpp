#include <opencv2/opencv.hpp>
#include <iostream>

int main() {
    // Read the image file
    cv::Mat image = cv::imread("../image.png");

    // Check for failure
    if (image.empty()) {
        std::cout << "Could not open or find the image" << std::endl;
        return -1;
    }

    // Display the image
    cv::imshow("Display window", image);

    // Wait for any keystroke
    cv::waitKey(0);

    return 0;
}

