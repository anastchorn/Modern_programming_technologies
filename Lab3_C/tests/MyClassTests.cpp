#define CATCH_CONFIG_MAIN  
#include "catch_amalgamated.hpp"
#include "MyClass.h"

TEST_CASE("Passing by value does not change the original object", "[value_type]") {
    MyClass obj(1);
    modifyByValue(obj);
    REQUIRE(obj.value == 1);
}

TEST_CASE("Passing by reference changes the original object", "[reference_type]") {
    MyClass obj(1);
    modifyByReference(obj);
    REQUIRE(obj.value == 200);
}

TEST_CASE("Objects created on the stack are destroyed automatically", "[stack]") {
    MyClass obj = createOnStack(10);
    REQUIRE(obj.value == 10);
}

TEST_CASE("Objects created on a hive are not automatically destroyed", "[heap]") {
    MyClass* obj = createOnHeap(20);
    REQUIRE(obj->value == 20);
    delete obj;
}
