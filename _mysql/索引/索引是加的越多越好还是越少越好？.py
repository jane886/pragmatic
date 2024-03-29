"""


1，索引是加的越多越好还是越少越好？
2，为什么加索引不能加过多？

    取决于实际需求。增加索引可以加快查询速度，但降低插入速度。这是一种 tradeoff，要根据实际情况权衡

    索引并不是加的越多越好，还是越少越好，而是需要根据具体的应用场景和数据特点来进行选择和优化

    如果索引过多，会导致以下问题：
    1，索引占用空间大：每个索引都需要占用磁盘空间，过多的索引会占用大量的空间，导致磁盘空间不足
    2，索引更新效率低：每次更新数据都需要更新索引，过多的索引会增加更新的时间和复杂性，降低更新效率
    3，查询优化器性能下降：查询优化器需要评估多个索引，选择最优的查询计划，过多的索引会增加查询优化器的计算复杂度，影响查询性能
    4，数据库维护难度大：过多的索引会增加数据库的维护难度和成本，如备份、恢复、重建等操作都需要考虑索引的影响

    而如果索引过少，会导致以下问题：
    1，查询效率低：查询需要扫描整个数据表，耗费大量的时间和资源，降低查询效率
    2，锁竞争激烈：查询需要对整个数据表进行锁定，导致锁资源激烈，降低并发性能
    3，内存使用率低：查询需要从磁盘读取数据，增加 IO 负载，降低内存使用率和性能

    因此，需要根据具体的应用场景和数据特点来选择和优化索引，一般来说，可以从以下几个方面入手：
    1，根据查询频率和条件选择索引：选择频繁使用的查询条件作为索引，避免过多的索引
    2，根据数据分布和查询类型来选择索引：选择数量分布均匀的列作为索引，避免重复和不必要的索引；
     同时，选择适合查询类型的索引，如范围查询、排序等
    3，合理利用复合索引：使用复合索引可以减少索引数量，提高查询效率
    4，定期维护和优化索引：定期检查和优化索引可以保持索引的有效性和性能，避免过多的索引和不必要的索引


"""