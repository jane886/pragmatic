"""

1，事务的特性：原子性、一致性、隔离性、持久性

2，多个事务执行的时候会发生的问题：脏读、幻读、不可重复读

3，事务的隔离级别
读未提交：一个事务的更改未提交，其他事务能看到更改
读提交：一个事务的更改提交后，其他事务才看到
可重复读：一个事务执行过程中看到的数据始终是一样的。另外为提交的更改对其他事务不可见
串行化：对一个事务的记录会加读写锁，有冲突的时候，下一个事务要等待前一个事务执行完后才可以执行

"""