"""


为什么读用 MyISAM

    读取操作通常是数据库中最常见的操作之一，MyISAM 在读取性能方面有一定的优势，这是因为 MyISAM 在缓存机制上与 InnoDB 有所不同

    MyISAM 只缓存索引，而不缓存数据，这意味着在进行大量的读取操作时，它可以使用更少的内存来缓存更多的数据，从而提高读取性能。
    此外，MyISAM 的索引结构相对简单，适用于全文搜索的场景，因为 MyISAM 支持全文索引

    因此，如果对数据的读取操作远多于写入操作，或者对数据一致性的要求不高，使用 MyISAM 可以获得更好的读取性能。但是，
    如果需要频繁地进行更新、插入或删除操作，则 InnoDB 的性能可能更佳，因为它使用更先进的缓存机制和行级锁定机制来处理
    数据的更新和写入操作

"""