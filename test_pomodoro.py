import os
from unittest import TestCase
import pomodoro


class PomodoroTest(TestCase):
    def test_play_alarm(self):
        pomodoro.play_alarm(pomodoro.ALARM_FILE)
