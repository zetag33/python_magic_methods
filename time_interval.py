class time_interval():
    
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    def __add__(self, other):
        if isinstance(other, time_interval):
            total_hours = self.hours + other.hours
            total_minutes = (total_hours * 60) + self.minutes + other.minutes
            total_seconds = total_minutes * 60 + self.seconds + other.seconds
            hours = total_seconds // 3600
            minutes = (total_seconds % 3600) // 60
            seconds = total_seconds % 60
            return hours, minutes, seconds
        elif isinstance(other, int):
            total_hours = self.hours
            total_minutes = (total_hours * 60) + self.minutes
            total_seconds = total_minutes * 60 + self.seconds
            total_seconds = total_seconds + other
            hours = total_seconds // 3600
            minutes = (total_seconds % 3600) // 60
            seconds = total_seconds % 60
            return hours, minutes, seconds            

        else:
            raise Exception('One of the objects was not of time_interval class')
    
    def __sub__(self, other):
        if isinstance(other, time_interval):
            total_seconds_self = self.hours * 3600 + self.minutes * 60 + self.seconds
            total_seconds_other = other.hours * 3600 + other.minutes * 60 + other.seconds
            total_seconds_diff = abs(total_seconds_self - total_seconds_other)
            hours = total_seconds_diff // 3600
            minutes = (total_seconds_diff % 3600) // 60
            seconds = total_seconds_diff % 60
            return hours, minutes, seconds
        elif isinstance(other, int):
            total_hours = self.hours
            total_minutes = (total_hours * 60) + self.minutes
            total_seconds = total_minutes * 60 + self.seconds
            total_seconds = total_seconds - other
            hours = total_seconds // 3600
            minutes = (total_seconds % 3600) // 60
            seconds = total_seconds % 60
            return hours, minutes, seconds  
        else:
            raise Exception('One of the objects was not of time_interval class')

    def __mul__(self, other):
        if isinstance(other, int):
            total_seconds_self = self.hours * 3600 + self.minutes * 60 + self.seconds
            total_seconds_return = total_seconds_self * other
            hours = total_seconds_return // 3600
            minutes = (total_seconds_return % 3600) // 60
            seconds = total_seconds_return % 60
            return hours, minutes, seconds
        else:
            raise Exception('You need to multiply by an integer')

    def __str__(self):
        hours = str(self.hours)
        minutes = str(self.minutes)
        seconds = str(self.seconds)
        return f"{hours}:{minutes}:{seconds}"
            
            
a1 = time_interval(1,1,1)
a2 = time_interval(23,23,23)

print(a1+a2)
print(a1-a2)
print(a1*3)
print(str(a1))
print(a1 + 1)
print(a2 -60)
print(a2-3600)
