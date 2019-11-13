from celery import Celery

# app = Celery('tasks', broker='redis://redis:6379/0')
# app = Celery('tasks',
#              broker='redis://localhost:6379/0',
#              backend="db+postgresql://pawkuk:pawel123@localhost/celery")


def make_celery(app):
    celery = Celery(app.import_name,
                    backend=app.config['CELERY_RESULT_BACKEND'],
                    broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery
