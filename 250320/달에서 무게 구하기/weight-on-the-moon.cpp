#include <iostream>
using namespace std;

int main() {
    float weight = 13;
    float gravity_ratio = 0.165;

    cout << weight;
    cout << " * ";
    cout << fixed;
    cout.precision(6);
    cout << gravity_ratio;
    cout << " = ";
    cout << weight * gravity_ratio;
    // Please write your code here.
    return 0;
}