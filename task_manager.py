from task import Task


class TaskManager:
    all_tasks = []

    def do_add_task(self, title, description, due_date):
        
        try:
            new_task = Task(title, description, due_date)
            self.all_tasks.append(new_task)
            print("Task Added Successfully")
        except TypeError as e:
            print("Error adding task {}".format(e))
    def do_update_task(self, title, attribute, new_val):
        task_to_update = None

        for task in self.all_tasks:
            if task.title == title:
                task_to_update = task
                break

        if task_to_update:
            if attribute == "Title":
                task_to_update.title = new_val
            elif attribute == "Description":
                task_to_update.description = new_val
            elif attribute == "Due_date":
                task_to_update.due_date = new_val
            elif attribute == "Status":
                task_to_update.status = new_val
            else:
                print("Invalid attribute specified")
        else:
            print(f"Task '{title}' not found")

    def do_delete_task(self, title):
        task_to_remove = None

        for task in self.all_tasks:
            if task.title == title:
                task_to_remove = task
                break

        if task_to_remove:
            self.all_tasks.remove(task_to_remove)
            print(f"Task '{title}' deleted successfully")
        else:
             print(f"Task '{title}' not found")

    def do_view_task(self):
        for task in self.all_tasks:
            task_info = task.to_dict()
            print(task_info)
            print("=" * 140)