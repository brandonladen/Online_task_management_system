
class Task:
    """A class"""
    next_priority = 0

    def __init__(self, title, description, due_date):
        """Class Task constructor"""
        self.__title = title
        self.__description = description
        self.__due_date = due_date
        self.priority = Task.next_priority
        Task.next_priority += 1
        self.status = "Pending"

    @property
    def title(self):
        """title gettter"""
        return self.__title
    
    @title.setter
    def title(self, val):
        """title setter"""
        self.__title = val

    @property
    def description(self):
        """description getter"""
        return self.__description
    
    @description.setter
    def description(self, val):
        """description setter"""
        self.__description = val

    @property
    def due_date(self):
        """due_date getter"""
        return self.__due_date
    
    @due_date.setter
    def due_date(self, val): # format of accepted date -> 21-04-2023
        """due_date setter"""
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
        """dictionary representation of class Task"""
        return {"Title": self.__title, 
                "Description": self.__description,
                 "Due_date": self.__due_date,
                 "Priority": self.priority,
                 "Status": self.status
                 }