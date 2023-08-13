
class Task:
    """A class"""
    next_priority = 0

    def __init__(self, title, description, due_date):
        """Class Task constructor"""
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = Task.next_priority
        Task.next_priority += 1
        self.status = "Pending"

    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, val):
        self.__title = val

    @property
    def description(self):
        return self.__description
    
    @description.setter
    def description(self, val):
        self.__description = val

    @property
    def due_date(self):
        return self.__due_date
    
    @due_date.setter
    def due_date(self, val): #21-04-2023
        if len(val.split("-")) < 3:
            raise TypeError("Wrong date format")
        elif len(val.split("-")[2]) != 4:
            raise TypeError("Wrong date format, check Year")
        elif int(val.split("-")[1]) > 12:
            raise TypeError("Wrong date format, check Month")
        elif int(val.split("-")[0]) > 31:
            raise TypeError("Wrong date format, check Day")
        else:
            self.__due_date = val

    def to_dict(self):
        return {"Title": self.__title, 
                "Description": self.__description,
                 "Due_date": self.__due_date,
                 "Priority": self.priority,
                 "Status": self.status
                 }