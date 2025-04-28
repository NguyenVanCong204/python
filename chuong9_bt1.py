from pydantic import BaseModel

class Schedule(BaseModel):
    courseName: str
    startTime: str
    endTime: str

class Person:
    def __init__(self, Name, Id, dept):
        self.Name = Name
        self.Id = Id
        self.dept = dept
        self.schedule = None  

    def getSchedule(self):
        
        return self.schedule
    def updateSchedule(self, courseName, startTime, endTime):
        self.schedule = Schedule(courseName=courseName, startTime=startTime, endTime=endTime)

person = Person("Công", 1, "22")

schedule = person.getSchedule("Python", "09:00", "11:00")

print("Schedule:", schedule,person.Name,person.Id,person.dept)
