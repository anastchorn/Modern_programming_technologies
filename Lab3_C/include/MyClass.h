#ifndef MYCLASS_H
#define MYCLASS_H

#include <iostream>

class MyClass {
public:
    int value;
    MyClass(int v);
    MyClass(const MyClass& other);
    ~MyClass();
};

void modifyByValue(MyClass c);
void modifyByReference(MyClass& c);
void modifyByPointer(MyClass* c);

#endif
