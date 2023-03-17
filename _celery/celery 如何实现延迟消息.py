"""
1，_celery 如何实现延迟消息
    # ETA 或 Countdown。
    # http://docs.celeryproject.org/en/latest/userguide/calling.html#calling-eta

    apply_async 执行方法可以设置额外的执行选项：
    ETA 是一个 datetime 对象，指定了任务执行的时间。
    Countdown 是一个整数，指定了任务执行的秒数。

    任务保证在指定日期和时间之后的某个时间执行，但不一定在那个确切时间执行。逾期的可能原因可能包括许多项目在队列中等待，或网络延迟时间长。

    带有eta或倒计时的任务会立即被 worker 获取，直到预定的时间过去，它们才会驻留在 worker 的内存中。
    此外，在工作人员开始执行任务之前，任务不会被确认。


    当使用这些选项为遥远的未来安排大量任务时，这些任务可能会在 worker 中累积并对 RAM 使用产生重大影响。
    因此，不推荐使用eta和countdown 来为遥远的未来安排任务。理想情况下，使用的值不要超过几分钟。

    当指定超过 15 分钟时使用 RabbitMQ 作为消息代理时countdown ，您可能会遇到 worker 终止并PreconditionFailed报错的问题：
    amqp.exceptions.PreconditionFailed: (0, 0): (406) PRECONDITION_FAILED - consumer ack timed out on channel

    在 RabbitMQ 中，自版本 3.8.15 以来，默认值为 consumer_timeout15 分钟。
    从版本 3.8.17 开始增加到 30 分钟。如果消费者在超过超时值的时间内未确认其交付，则其通道将因PRECONDITION_FAILED通道异常而关闭。
    有关详细信息，请参阅传递确认超时。

    要解决这个问题，在 RabbitMQ 配置文件中，rabbitmq.conf您应该指定consumer_timeout参数大于或等于您的倒计时值。
    例如，您可以指定一个非常大的值，等于 1 年（以毫秒为单位），以避免将来出现问题。consumer_timeout = 31622400000



2，时间的延迟如何做到？是在到了时间后放入 worker 还是一开始就通知 woker，让其自动计时。

    时间到了才会执行，原因见上图（celery文档中ETA的描述）。



3，消息队列的时间控制机制具体如何执行，如果一开始是存在1小时之后执行的任务，然后来了一些需要立马执行的任务，此时是什么样的安排方式？

    需要立马执行的任务立马执行，同时延时任务继续计时，这个计时是保证任务不在 1 小时之内执行，而不是精确地在 1 小时后的那个点上执行，
    如果发生任务堆积，延时任务会在队列中等待。

"""


from datetime import timedelta
from time import timezone

from celery import Celery
from celery.utils.log import get_task_logger

app = Celery('worker')
logger = get_task_logger(__name__)


@app.task(bind=True)
# bind 参数意味着该函数将是一个“绑定方法”，以便您可以访问任务类型实例上的属性和方法。
def add(self, x, y):
    logger.info('Request: {0!r}'.format(self.request))
    return x + y


# Countdown
# Countdown 是一个整数，指定了任务执行的秒数。
# 例如，如果你想在 10 秒后执行一个任务，你可以这样做：
result1 = add.apply_async((2, 2), countdown=10)
print("result", result1)


# ETA
# ETA 是一个 datetime 对象，指定了任务执行的时间。
# 例如，如果你想在 30 秒后执行一个任务，你可以这样做：
result2 = add.apply_async((2, 2), eta=timezone.now() + timedelta(seconds=30))
print("result2", result2)
