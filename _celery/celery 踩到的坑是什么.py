"""


1，celery 踩到的坑是什么

    1, 当使用 Redis 作为中间件时，有一个 visibility_timeout （可见性超时）默认为一小时。
    在设置了延时任务的时候，如果任务没有在 visibility_timeout 时间内 ack，就会被重新分发到另一个 worker 去执行。

    这意味着如果设置了超过一小时的延时任务，会导致重复执行。
    解决方案是把 visibility timeout 设置到最够大，或在任务中做排重校验。


    2, 从 Celery 3.1 开始，worker 除了会从 broker 获取任务, 还会被动地订阅其他 worker 事件，比如心跳,
    在 worker 很多的情况下, 会导致 worker  处理真正的任务变少, 导致任务堆积，
    添加 Gossip 是为了让 celery 用户可以利用工作人员的沟通，比如将任务重新路由给最好的工作人员，但是如果工作人员没有理由进行交流，可以禁用它。
    添加--without-mingle选项以在启动时禁用 worker 同步

    所以一般启动 worker 的时候都会带上 --without-mingle --without-gossip --without-heartbeat 这些 tag
    添加--without-mingle选项以在启动时禁用 worker 同步
    https://stackoverflow.com/questions/50328971/celery-disable-heartbeat-between-workers

"""