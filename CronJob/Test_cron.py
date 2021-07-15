import unittest
import CronJob


class TestCron(unittest.TestCase):

    def test_check_time(self):
        self.assertRaises(Exception, CronJob.check_time("1:2"))
        self.assertRaises(Exception, CronJob.check_time("5:55"))

    def test_calculate_time(self):
        daily = "/bin/run_me_daily"
        hourly = "/bin/run_me_hourly"
        minute = "/bin/run_me_every_minute"
        sixty = "/bin/run_me_sixty_times"

        self.assertRaises(Exception, "01:30 today - " + daily, CronJob.calculate_time("1", "30", daily, "0:3"))

        self.assertEqual("01:30 today - " + daily, CronJob.calculate_time("1", "30", daily, "00:30"))
        self.assertEqual("01:30 tomorrow - " + daily, CronJob.calculate_time("1", "30", daily, "10:30"))
        self.assertEqual("01:30 today - " + daily, CronJob.calculate_time("1", "30", daily, "01:29"))
        self.assertEqual("01:30 tomorrow - " + daily, CronJob.calculate_time("1", "30", daily, "01:31"))
        self.assertEqual("01:30 tomorrow - " + daily, CronJob.calculate_time("1", "30", daily, "20:30"))
        self.assertEqual("01:30 tomorrow - " + daily, CronJob.calculate_time("1", "30", daily, "23:00"))
        self.assertEqual("01:30 tomorrow - " + daily, CronJob.calculate_time("1", "30", daily, "23:50"))
        self.assertEqual("01:30 today - " + daily, CronJob.calculate_time("1", "30", daily, "00:00"))

        self.assertEqual("00:45 today - " + hourly, CronJob.calculate_time("*", "45", hourly, "00:30"))
        self.assertEqual("10:45 today - " + hourly, CronJob.calculate_time("*", "45", hourly, "10:30"))
        self.assertEqual("01:45 today - " + hourly, CronJob.calculate_time("*", "45", hourly, "01:29"))
        self.assertEqual("01:45 today - " + hourly, CronJob.calculate_time("*", "45", hourly, "01:31"))
        self.assertEqual("17:45 today - " + hourly, CronJob.calculate_time("*", "45", hourly, "17:40"))
        self.assertEqual("18:45 today - " + hourly, CronJob.calculate_time("*", "45", hourly, "17:50"))
        self.assertEqual("23:45 today - " + hourly, CronJob.calculate_time("*", "45", hourly, "23:00"))
        self.assertEqual("00:45 tomorrow - " + hourly, CronJob.calculate_time("*", "45", hourly, "23:50"))

        self.assertEqual("00:30 today - " + minute, CronJob.calculate_time("*", "*", minute, "00:30"))
        self.assertEqual("10:30 today - " + minute, CronJob.calculate_time("*", "*", minute, "10:30"))
        self.assertEqual("01:29 today - " + minute, CronJob.calculate_time("*", "*", minute, "01:29"))
        self.assertEqual("01:31 today - " + minute, CronJob.calculate_time("*", "*", minute, "01:31"))
        self.assertEqual("20:30 today - " + minute, CronJob.calculate_time("*", "*", minute, "20:30"))
        self.assertEqual("23:00 today - " + minute, CronJob.calculate_time("*", "*", minute, "23:00"))
        self.assertEqual("00:00 today - " + minute, CronJob.calculate_time("*", "*", minute, "00:00"))

        self.assertEqual("19:00 today - " + sixty, CronJob.calculate_time("19", "*", sixty, "00:30"))
        self.assertEqual("19:00 today - " + sixty, CronJob.calculate_time("19", "*", sixty, "10:30"))
        self.assertEqual("19:00 today - " + sixty, CronJob.calculate_time("19", "*", sixty, "01:29"))
        self.assertEqual("19:00 tomorrow - " + sixty, CronJob.calculate_time("19", "*", sixty, "19:30"))
        self.assertEqual("19:00 tomorrow - " + sixty, CronJob.calculate_time("19", "*", sixty, "19:45"))
        self.assertEqual("19:00 tomorrow - " + sixty, CronJob.calculate_time("19", "*", sixty, "23:00"))
        self.assertEqual("19:00 today - " + sixty, CronJob.calculate_time("19", "*", sixty, "00:00"))


if __name__ == '__main__':
    unittest.main()
