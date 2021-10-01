"""Module for time-related functionality"""
import datetime
import time


class Rate:
    """
    Convenience class for sleeping in a loop at a specific rate
    """

    def __init__(self, freq: float) -> None:
        self.last_time = None
        self.sleep_duration = datetime.timedelta(seconds=(1.0 / freq))

    def remaining(self) -> None:
        """
        Calculates the time remaining for the object to sleep

        Adapted from:
        https://docs.ros.org/en/lunar/api/rospy/html/rospy.timer.Rate-class.html
        """
        current_time = datetime.datetime.now()
        return self._remaining(current_time)

    def sleep(self) -> None:
        """
        Best-effort method to sleep for the specified amount of time

        Adapted from:
        https://docs.ros.org/en/lunar/api/rospy/html/rospy.timer.Rate-class.html
        """
        current_time = datetime.datetime.now()

        if self.last_time is None:
            self.last_time = datetime.datetime.now()

        sleep_time = self.sleep_duration - (current_time - self.last_time)
        if sleep_time > 0:
            time.sleep(sleep_time)

        self.last_time = datetime.datetime.now()

    def _remaining(self, current_time):
        """
        Calculate the time remaining for rate to sleep

        Adapted from:
        https://docs.ros.org/en/lunar/api/rospy/html/rospy.timer.Rate-class.html
        """
        # detect time jumping backwards
        if self.last_time > current_time:
            self.last_time = current_time

        # calculate remaining time
        elapsed = current_time - self.last_time
        return self.sleep_dur - elapsed
