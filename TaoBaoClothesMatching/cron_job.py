from crontab import CronTab


cron = CronTab(user='taobao')
job = cron.new(command='python offline_trainer.py')
job.day.every(1)

cron.write()
