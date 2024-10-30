import tkinter as tk
from tkinter import messagebox

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Not Completed"
        return f"{self.title}: {self.description} - Due: {self.due_date} - {status}"

class ToDoListGUI:
    def __init__(self, root):
        self.root = root
        self.tasks = []
        self.task_index = 0

        # Set background color for the main window
        self.root.configure(bg="#f0f8ff")  # Light blue background

        # Create task frame
        self.task_frame = tk.Frame(self.root, bg="#f0f8ff")
        self.task_frame.pack(fill="both", expand=True)

        # Create task title label and entry
        self.task_title_label = tk.Label(self.task_frame, text="Task Title:", bg="#f0f8ff", fg="#333333")
        self.task_title_label.pack()
        self.task_title_entry = tk.Entry(self.task_frame, bg="#ffffff", fg="#000000")
        self.task_title_entry.pack()

        # Create task description label and entry
        self.task_description_label = tk.Label(self.task_frame, text="Task Description:", bg="#f0f8ff", fg="#333333")
        self.task_description_label.pack()
        self.task_description_entry = tk.Entry(self.task_frame, bg="#ffffff", fg="#000000")
        self.task_description_entry.pack()

        # Create due date label and entry
        self.due_date_label = tk.Label(self.task_frame, text="Due Date (YYYY-MM-DD):", bg="#f0f8ff", fg="#333333")
        self.due_date_label.pack()
        self.due_date_entry = tk.Entry(self.task_frame, bg="#ffffff", fg="#000000")
        self.due_date_entry.pack()

        # Create buttons frame
        self.buttons_frame = tk.Frame(self.root, bg="#f0f8ff")
        self.buttons_frame.pack(fill="x")

        # Create buttons with colors
        button_color = "#008CBA"  # Blue color for buttons
        self.create_task_button = tk.Button(self.buttons_frame, text="Create Task", command=self.create_task, bg=button_color, fg="white")
        self.create_task_button.pack(side="left", padx=5, pady=5)

        self.view_tasks_button = tk.Button(self.buttons_frame, text="View Tasks", command=self.view_tasks, bg=button_color, fg="white")
        self.view_tasks_button.pack(side="left", padx=5, pady=5)

        self.update_task_button = tk.Button(self.buttons_frame, text="Update Task", command=self.update_task, bg=button_color, fg="white")
        self.update_task_button.pack(side="left", padx=5, pady=5)

        self.delete_task_button = tk.Button(self.buttons_frame, text="Delete Task", command=self.delete_task, bg=button_color, fg="white")
        self.delete_task_button.pack(side="left", padx=5, pady=5)

        self.mark_task_as_completed_button = tk.Button(self.buttons_frame, text="Mark Task as Completed", command=self.mark_task_as_completed, bg=button_color, fg="white")
        self.mark_task_as_completed_button.pack(side="left", padx=5, pady=5)

        # Create tasks listbox with colors
        self.tasks_listbox = tk.Listbox(self.root, bg="#ffffff", fg="#000000", selectbackground="#cce5ff", selectforeground="#000000")
        self.tasks_listbox.pack(fill="both", expand=True)

    def create_task(self):
        title = self.task_title_entry.get()
        description = self.task_description_entry.get()
        due_date = self.due_date_entry.get()
        if title and description and due_date:
            new_task = Task(title, description, due_date)
            self.tasks.append(new_task)
            self.tasks_listbox.insert("end", str(new_task))
            self.task_title_entry.delete(0, "end")
            self.task_description_entry.delete(0, "end")
            self.due_date_entry.delete(0, "end")
        else:
            messagebox.showerror("Error", "Please enter all fields.")

    def view_tasks(self):
        self.tasks_listbox.delete(0, "end")
        for task in self.tasks:
            self.tasks_listbox.insert("end", str(task))

    def update_task(self):
        try:
            self.task_index = self.tasks_listbox.curselection()[0]
            title = self.task_title_entry.get()
            description = self.task_description_entry.get()
            due_date = self.due_date_entry.get()
            if title and description and due_date:
                self.tasks[self.task_index].title = title
                self.tasks[self.task_index].description = description
                self.tasks[self.task_index].due_date = due_date
                self.tasks_listbox.delete(self.task_index)
                self.tasks_listbox.insert(self.task_index, str(self.tasks[self.task_index]))
                self.task_title_entry.delete(0, "end")
                self.task_description_entry.delete(0, "end")
                self.due_date_entry.delete(0, "end")
            else:
                messagebox.showerror("Error", "Please enter all fields.")
        except IndexError:
            messagebox.showerror("Error", "Select a task to update.")

    def delete_task(self):
        try:
            self.task_index = self.tasks_listbox.curselection()[0]
            self.tasks_listbox.delete(self.task_index)
            del self.tasks[self.task_index]
        except IndexError:
            messagebox.showerror("Error", "Select a task to delete.")

    def mark_task_as_completed(self):
        try:
            self.task_index = self.tasks_listbox.curselection()[0]
            self.tasks[self.task_index].mark_as_completed()
            self.tasks_listbox.delete(self.task_index)
            self.tasks_listbox.insert(self.task_index, str(self.tasks[self.task_index]))
        except IndexError:
            messagebox.showerror("Error", "Select a task to mark as completed.")

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")
app = ToDoListGUI(root)
root.mainloop()