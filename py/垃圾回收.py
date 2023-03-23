"""


垃圾回收是指自动识别和释放不再使用的内存空间的过程。在程序运行过程中，动态分配的内存空间可能会变得无用或者不再被访问，
但是这些内存空间却没有被显式地释放，这就会导致内存泄漏和程序的运行效率低下。

垃圾回收通过识别这些无用的内存空间，将它们从程序中释放出来，从而提高程序的运行效率和稳定性


垃圾回收的实现方式：
1，引用计数：通过记录每个对象被引用的次数来判断对象是否可以被释放。当对象的引用计数为 0 时，就可以将这个对象释放

2，标记-清除：这种算法通过标记所有可以访问的对象，并清除所有不可访问的对象来实现垃圾回收。
    主要缺点是会产生内存碎片

3，分代垃圾回收：这种算法将内存空间分为多个代，每个代中的对象有不同的生命周期。
    同时，它也采用了多种垃圾回收算法，使得每个代的垃圾回收效率更高

4，增量垃圾回收：这种算法将垃圾回收的过程中分解成多个阶段，每个阶段只回收部分垃圾，从而减少了垃圾回收对程序运行的影响

Python 采用了引用计数和标记-清除两种垃圾回收算法。同时，Python 还使用了循环垃圾回收算法，以解决因循环引用导致的内存泄漏问题，
循环垃圾回收算法主要是在标记=清除算法的基础上，增加了对循环引用的处理，通过引入弱引用等机制来解决引用导致的内存泄漏问题



"""