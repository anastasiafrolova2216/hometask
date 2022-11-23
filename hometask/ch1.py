class Ch1:

    @staticmethod
    def BMI(weight: float, height: float) -> str:
        bmi = weight / height ** 2

        if bmi > 24.99:
            return "Избыточная масса тела."
        elif bmi < 18.5:
            return "Недостаточная масса тела."
        else:
            return "Норма."

    @staticmethod
    def Teacher(hour: int, minutes: int) -> str:
        if hour > 23 or minutes > 59:
            raise ValueError('Max time in format program: 23h 59m')

        import datetime
        import time

        def stts(str_time: str) -> float:
            time_obj = time.strptime(str_time, '%H:%M')
            return datetime.timedelta(
                hours=time_obj.tm_hour,
                minutes=time_obj.tm_min,
                seconds=time_obj.tm_sec
            ).total_seconds()

        ust = "%s:%s" % (hour, minutes)

        if 0 \
                or (stts('10:30') <= stts(ust) and stts(ust) < stts('12:00')) \
                or (stts('13:40') <= stts(ust) and stts(ust) < stts('15:00')) \
                or (stts('18:00') <= stts(ust) and stts(ust) < stts('19:30')):
            return "Преподаватель занят."
        elif 0 \
                or (0 <= stts(ust) and stts(ust) < stts('10:30')) \
                or (stts('20:00') <= stts(ust)):
            return "Преподаватель занят."
        else:
            return "Преподаватель свободен."

    @staticmethod
    def ListSV() -> int:
        return 0 \
            + sum([n**3 for n in range(18, 37) if n % 3 == 0]) \
            + sum([n**2 for n in range(18, 37) if n % 2 == 0])
