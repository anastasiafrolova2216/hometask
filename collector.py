from hometask.ch1 import Ch1
import sys


if __name__ == "__main__":
    args = sys.argv

    task_list = {
        1: {
            'Env': [
                lambda: float(input("Введите вес (кг.): ")),
                lambda:  float(input("Введите рост (м.): "))
            ],
            'Fn': Ch1.BMI
        },
        2: {
            'Env': [
                lambda: int(input("Введите час: ")),
                lambda:  int(input("Введите минуты: "))
            ],
            'Fn': Ch1.Teacher
        },
        3: {
            'Env': [],
            'Fn': Ch1.ListSV
        }
    }

    task = int(args[1])

    try:
        task_arg = list(map((lambda fn: fn()), task_list[task]['Env']))
        result = task_list[task]['Fn'](*task_arg)
        print(result)
    except KeyError as e:
        raise ValueError('Undefined task: {}'.format(e.args[0]))


else:
    raise ValueError('Sorry! Run main')
