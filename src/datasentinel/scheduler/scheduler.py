from apscheduler.schedulers.blocking import BlockingScheduler

from datasentinel.engine import DataSentinelEngine


class ValidationScheduler:

    def __init__(self):

        self.scheduler = BlockingScheduler()

    def schedule_validation(
        self,
        source_type,
        source_path,
        rule_file,
        interval_minutes,
    ):

        self.scheduler.add_job(
            self.run_validation,
            "interval",
            minutes=interval_minutes,
            args=[
                source_type,
                source_path,
                rule_file,
            ],
        )

        print(
            f"Validation scheduled every {interval_minutes} minute(s)."
        )

        self.scheduler.start()

    @staticmethod
    def run_validation(
        source_type,
        source_path,
        rule_file,
    ):

        print("Running Scheduled Validation...")

        engine = DataSentinelEngine()

        engine.run(
            source_type,
            source_path,
            rule_file,
        )

        print("Validation Finished.\n")