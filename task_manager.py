from task import Task


class TaskManager:
    all_tasks = []

    def do_add_task(self, title, description, due_date):
        """A method that adds a new task to all_tasks list"""
        try:
            new_task = Task(title, description, due_date)
            self.all_tasks.append(new_task)
            print("Task Added Successfully")
        except TypeError as e:
            print("Error adding task {}".format(e))
            
    def do_update_task(self, title, attribute, new_val):
        """A method that updates any attribute except priority"""
        task_to_update = None

        for task in self.all_tasks:
            if task.title == title:
                task_to_update = task
                break

        if task_to_update:
            if attribute == "Title":
                task_to_update.title = new_val
                print("Updated Successfully")
            elif attribute == "Description":
                task_to_update.description = new_val
                print("Updated Successfully")
            elif attribute == "Due_date":
                task_to_update.due_date = new_val
                print("Updated Successfully")
            elif attribute == "Status":
                task_to_update.status = new_val
                print("Updated Successfully")
            else:
                print("Invalid attribute specified")
        else:
            print("Task '{}' not found".format(title))

    def do_delete_task(self, title):
        """A method thats deletes a task that whose title has been provided by the user"""
        task_to_remove = None

        for task in self.all_tasks:
            if task.title == title:
                task_to_remove = task
                break

        if task_to_remove:
            self.all_tasks.remove(task_to_remove)
            print("Task '{}' deleted successfully".format(title))
        else:
             print("Task '{}' not found". format(title))

    def do_view_task(self):
        """A method that prints a task in dictionary representation"""
        for task in self.all_tasks:
            task_info = task.to_dict()
            print(task_info)
            print("=" * 110)
