#define CATCH_CONFIG_MAIN  
#include "catch_amalgamated.hpp"
#include "MyClass.h"
#include <iostream>
#include <vector>

#ifdef _WIN32
#include <windows.h>
#include <psapi.h>
#else
#include <sys/resource.h>
#include <unistd.h>
#endif

size_t getHeapSize() {
#ifdef _WIN32
    PROCESS_MEMORY_COUNTERS info;
    GetProcessMemoryInfo(GetCurrentProcess(), &info, sizeof(info));
    return info.WorkingSetSize;
#else
    struct rusage r_usage;
    getrusage(RUSAGE_SELF, &r_usage);
    return r_usage.ru_maxrss;
#endif
}

TEST_CASE("Object is created on the stack", "[stack]") {
    size_t heap_before = getHeapSize();
    {
        MyClass obj(10);  
    }
    size_t heap_after = getHeapSize();

    std::cout << "Heap size before: " << heap_before << "\n";
    std::cout << "Heap size after stack allocation: " << heap_after << "\n";

    REQUIRE(heap_before == heap_after);  
}

TEST_CASE("Object is created on the heap", "[heap]") {
    size_t heap_before = getHeapSize();
    std::vector<MyClass*> objects;
    for (int i = 0; i < 1000; ++i) {
        objects.push_back(new MyClass(20));  
    }
    size_t heap_after = getHeapSize();

    std::cout << "Heap size before: " << heap_before << "\n";
    std::cout << "Heap size after allocation: " << heap_after << "\n";

    REQUIRE(heap_before < heap_after);  

    for (auto obj : objects) {
        delete obj;
    }
    size_t heap_after_delete = getHeapSize();

    std::cout << "Heap size after deletion: " << heap_after_delete << "\n";
}

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
    MyClass obj = MyClass(10);
    REQUIRE(obj.value == 10);
}

TEST_CASE("Objects created on the heap are not automatically destroyed", "[heap]") {
    MyClass* obj = new MyClass(20);
    REQUIRE(obj->value == 20);
    delete obj;
}

TEST_CASE("Multiple objects created on the stack", "[stack_multiple]") {
    size_t heap_before = getHeapSize();
    for (int i = 0; i < 10000; ++i) {
        MyClass obj(10); 
    }
    size_t heap_after = getHeapSize();

    std::cout << "Heap size before: " << heap_before << "\n";
    std::cout << "Heap size after multiple stack allocations: " << heap_after << "\n";

    REQUIRE(heap_before == heap_after);  
}

TEST_CASE("Multiple objects created on the heap", "[heap_multiple]") {
    const int num_objects = 10000;
    MyClass* objects[num_objects];

    size_t heap_before = getHeapSize();
    for (int i = 0; i < num_objects; ++i) {
        objects[i] = new MyClass(i);
    }
    size_t heap_after_allocations = getHeapSize();

    for (int i = 0; i < num_objects; ++i) {
        delete objects[i];
    }
    size_t heap_after_deletions = getHeapSize();

    std::cout << "Heap size before: " << heap_before << "\n";
    std::cout << "Heap size after allocations: " << heap_after_allocations << "\n";
    std::cout << "Heap size after deletions: " << heap_after_deletions << "\n";

    REQUIRE(heap_before < heap_after_allocations);
    REQUIRE(heap_after_deletions <= heap_after_allocations);
}
