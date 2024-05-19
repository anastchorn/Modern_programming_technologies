LAB3_C++
This project demonstrates the use of the MyClass class, which includes constructors, a destructor, and functions for modifying objects. The main focus is on testing the behavior of objects created on the stack and heap, as well as checking the passing of objects by value and by reference.

Description of MyClass

The MyClass class includes:
A constructor that initializes the value variable.

A copy constructor that outputs a message when an object is copied.

A destructor that outputs a message when an object is destroyed.

Functions modifyByValue, modifyByReference, and modifyByPointer to demonstrate passing objects by value, by reference, and by pointer.

Project Files
MyClass.h: Declaration of the MyClass class.
MyClass.cpp: Definition of the MyClass class functions.
main.cpp: Tests to verify object behavior.
Tests
The tests are written using the Catch2 library. They verify various aspects of working with MyClass objects.

List of Tests
Object is created on the stack

Verifies that creating an object on the stack does not change the heap size.
Object is created on the heap

Verifies that creating an object on the heap increases the heap size, and deleting it decreases the heap size.
Passing by value does not change the original object

Verifies that passing an object by value does not change the original object.
Passing by reference changes the original object

Verifies that passing an object by reference changes the original object.
Objects created on the stack are destroyed automatically

Verifies that objects on the stack are automatically destroyed when going out of scope.
Objects created on the heap are not automatically destroyed

Verifies that objects on the heap are not automatically destroyed and require manual deletion.
Multiple objects created on the stack

Verifies that creating many objects on the stack does not change the heap size.
Multiple objects created on the heap

Verifies that creating many objects on the heap increases the heap size, and deleting them decreases the heap size.

Explanation of the "Multiple objects created on the heap" Test
In the "Multiple objects created on the heap" test, we create a large number of objects on the heap and then delete them. The memory usage before and after these operations is measured. 


Here are the observations:

Memory Usage Before:

The initial memory usage before any allocations.
Memory Usage After Allocations:

Memory usage after allocating a large number of objects on the heap. As expected, the memory usage increases significantly.
Memory Usage After Deletions:

Memory usage after deleting the allocated objects. The memory usage decreases, but it may still be higher than the initial memory usage.




Why Memory Behavior is Observed this Way

Memory Allocators:

Memory allocators in modern operating systems often retain freed memory for reuse rather than returning it to the system immediately. This reduces the overhead of frequent system calls for memory allocation and deallocation.

Heap Fragmentation:

When objects are deleted, the memory they occupied may be fragmented. This fragmentation can make it difficult for the allocator to coalesce free memory blocks into larger contiguous blocks, resulting in higher memory usage even after deletions.

Internal Memory Management:

The memory allocator maintains internal data structures to manage free and allocated memory blocks. These structures can contribute to the observed memory usage.