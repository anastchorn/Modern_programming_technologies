#include "MyClass.h"

MyClass::MyClass(int v) : value(v) {}

MyClass::MyClass(const MyClass& other) : value(other.value) {
    std::cout << "Copy constructor called\n";
}

void modifyByValue(MyClass c) {
    c.value = 100;
}

void modifyByReference(MyClass& c) {
    c.value = 200;
}

MyClass createOnStack(int value) {
    return MyClass(value);
}

MyClass* createOnHeap(int value) {
    return new MyClass(value);
}
