from work_out import WorkOut
from work_out_types import WORK_OUT_TYPES_BY_DICT


def get_workout_type_from_user():
    while True:
        try:
            workout_type_input = input(
                "Please choose the workout type: (SC-23 or HIIT-7/4) "
            )
            return WORK_OUT_TYPES_BY_DICT[workout_type_input]
        except KeyError:
            print("You entered an invalid workout type!")


work_out_selection = get_workout_type_from_user()
workout = WorkOut(work_out_selection)
workout.start_work_out()
