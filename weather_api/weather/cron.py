from django_cron import CronJobBase, Schedule

from .utils import fetch_forecasts


class FetchStatisticsJob(CronJobBase):
    RUN_AT_TIMES = ['00:30']

    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = 'weather.fetch_data'

    def do(self):
        fetch_forecasts()
