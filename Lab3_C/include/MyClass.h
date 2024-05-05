#pragma once

#include <iostream>

class MyClass {
public:
    int value;
    MyClass(int v);
    MyClass(const MyClass& other);
};

void modifyByValue(MyClass c);
void modifyByReference(MyClass& c);
MyClass createOnStack(int value);
MyClass* createOnHeap(int value);
