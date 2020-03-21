import time
from playsound import playsound

LOCAL_PATH = '/Users/onurhunce/Desktop/beat81_simulator/'


class WorkOut:
    def __init__(self, work_out_type):
        self.SINGLE_WORKOUT_TIME_IN_SECONDS = (
            work_out_type['SINGLE_WORKOUT_TIME_IN_SECONDS']
        )
        self.BREAK_TIME_BETWEEN_WORKOUTS_IN_SECONDS = (
            work_out_type['BREAK_TIME_BETWEEN_WORKOUTS_IN_SECONDS']
        )
        self.BREAK_TIME_BETWEEN_ROUNDS_IN_SECONDS = (
            work_out_type['BREAK_TIME_BETWEEN_ROUNDS_IN_SECONDS']
        )
        self.WORK_OUT_NUMBER_PER_SESSION = (
            work_out_type['WORK_OUT_NUMBER_PER_SESSION']
        )
        self.TOTAL_NUMBER_OF_ROUNDS = (
            work_out_type['TOTAL_NUMBER_OF_ROUNDS']
        )

    def start_work_out(self):
        # Wait for 10 seconds in the beginning
        time.sleep(10)
        for i in range(self.TOTAL_NUMBER_OF_ROUNDS):
            self.execute_one_round()
            self.play_sound_for_long_break()
            print("ROUND IS COMPLETED \n")

    def execute_one_round(self):
        for i in range(self.WORK_OUT_NUMBER_PER_SESSION):
            print(f"workout {i + 1}")
            playsound(f"{LOCAL_PATH}sounds/workout_start.mp3")
            self.play_sound_for_round_end()
            self.sleep_during_short_break()
            print("\n")

    def play_sound_for_round_end(self):
        # Play countdown in last 5 seconds
        waiting_time = self.SINGLE_WORKOUT_TIME_IN_SECONDS - 5
        time.sleep(waiting_time)
        playsound(f"{LOCAL_PATH}sounds/workout_last_5.mp3")

    def sleep_during_short_break(self):
        time.sleep(self.BREAK_TIME_BETWEEN_WORKOUTS_IN_SECONDS)

    def play_sound_for_long_break(self):
        # Play countdown in last 5 seconds
        waiting_time = self.BREAK_TIME_BETWEEN_ROUNDS_IN_SECONDS - 5
        time.sleep(waiting_time)
        playsound(f"{LOCAL_PATH}sounds/break_last_5.mp3")