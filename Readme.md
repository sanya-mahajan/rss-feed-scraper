Celery is a task management system, it operates in conjunction with a message broker to carry out asynchronous work.

The scheduler (Celery beat) will execute these as cron jobs for us, without any extra work or interaction outside starting the Celery app.

systemctl start rabbitmq-server
