#include "MyClass.h"
#include <iostream>

MyClass::MyClass(int v) : value(v) {}

MyClass::MyClass(const MyClass& other) : value(other.value) {
    std::cout << "Copy constructor called\n";
}

MyClass::~MyClass() {
    std::cout << "Destructor called\n";
}

void modifyByValue(MyClass c) {
    c.value = 100;
}

void modifyByReference(MyClass& c) {
    c.value = 200;
}

void modifyByPointer(MyClass* c) {
    c->value = 300;
}
