"""

1，更新 MySQL
物理日志 redo log，InnoDB 引擎所有
逻辑日志 binlog，MySQL Server 层实现，所有引擎可以用

两阶段提交：
    redo log 记录后，状态为 prepare
    binlog 记录
    提交事务修改，redo log 更改状态为 commit

如果不用两阶段提交
1，先写 redo log，后写 binlog 失败，说明数据库的值已被更改，这样使用 binlog 恢复备份的时候就会导致与原数据库值不一致
2，先写 binlog，后写 redo log，事务回滚，数据库的值没变动，使用 binlog 恢复备份的时候新数据变了，跟原数据库不一致


"""