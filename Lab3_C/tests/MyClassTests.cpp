#define CATCH_CONFIG_MAIN  
#include "catch_amalgamated.hpp"
#include "MyClass.h"

TEST_CASE("Передача за значенням не змінює оригінальний об'єкт", "[value_type]") {
    MyClass obj(1);
    modifyByValue(obj);
    REQUIRE(obj.value == 1);
}

TEST_CASE("Передача посиланням змінює оригінальний об'єкт", "[reference_type]") {
    MyClass obj(1);
    modifyByReference(obj);
    REQUIRE(obj.value == 200);
}

TEST_CASE("Об'єкти створені на стеку знищуються автоматично", "[stack]") {
    MyClass obj = createOnStack(10);
    REQUIRE(obj.value == 10);
}

TEST_CASE("Об'єкти створені на хіпі не знищуються автоматично", "[heap]") {
    MyClass* obj = createOnHeap(20);
    REQUIRE(obj->value == 20);
    delete obj;
}
