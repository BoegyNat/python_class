#include <iostream>
using namespace std;

int main() {
    int choice;

    cout << "===== Roles =====" << endl;
    cout << "1. Assasin" << endl;
    cout << "2. Tank" << endl;
    cout << "3. Carry" << endl;
    cout << "4. Mage" << endl;
    cout << "Enter your choice (1-4): ";
    cin >> choice;

    switch (choice) {
        case 1:
            cout << "You chose Assasin" << endl;
            break;
        case 2:
            cout << "You chose Tank" << endl;
            break;
        case 3:
            cout << "You chose Carry" << endl;
            break;
        case 4:
            cout << "You chose Mage" << endl;
            break;
        default:
            cout << "Invalid choice!" << endl;
    }

    return 0;
}
