import time
import uuid
import datetime

from celerybeatmongo.models import PeriodicTask

from app import task, Result


PeriodicTask.objects.delete()
Result.objects.delete()


def get_name(name):
    return '%s:%s:%s' % (name, datetime.datetime.now().isoformat(),
                         uuid.uuid4().hex)


def test_max_run_count():
    name = get_name('test_max_run_count')
    PeriodicTask(
        name=name,
        task='app.task',
        args=(name, ),
        kwargs={},
        enabled=True,
        interval=PeriodicTask.Interval(every=1, period='seconds'),
        max_run_count=3,
        run_immediately=True,
    ).save()
    time.sleep(5)
    results = list(Result.objects(name=name))
    for result in results:
        print result
    assert len(results) == 3
