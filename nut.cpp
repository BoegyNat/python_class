#include <iostream>
#include <vector>

const int N = 10; // Example size, adjust as needed
const int M = 10; // Example size, adjust as needed

void updateImage(bool image[][M], int brushSize, int centerX, int centerY) {
    for (int i = -brushSize; i <= brushSize; i++) {
        for (int j = -brushSize; j <= brushSize; j++) {
            if (i * i + j * j <= brushSize * brushSize) {
                int x = centerX + i;
                int y = centerY + j;
                if (x >= 0 && x < N && y >= 0 && y < M) {
                    image[x][y] = true;
                }
            }
        }
    }
}

int main() {
    bool image[N][M] = {false};
    int brushSize = 2;
    int centerX = 5;
    int centerY = 5;

    updateImage(image, brushSize, centerX, centerY);

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            std::cout << (image[i][j] ? "*" : " ");
        }
        std::cout << std::endl;
    }

    return 0;
}