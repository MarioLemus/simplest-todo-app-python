from datetime import datetime
import sys
import variables

class Todo:
  def __init__(self):
    self.todos = []

  def get_data_from_user(self):
    print(f"{variables.log_welcome} \n")
    print(variables.log_instruct_new_todo)

    while(True):
        print(variables.log_input_title)
        title = input()
      
        while(len(title) < 1):
            print(variables.log_error_input_title)
            print(variables.log_input_title)
            title = input()

        print(variables.log_input_desc)
        description = input()

        if (len(description) < 1):
            description = f"{variables.log_default_desc_text} \n"

        self.save_todo_data(title, description)
        
        print(variables.log_response_success)
        print(variables.log_new_todo_question)
  
        response = input().lower()
        
        if (response != "y"):
            break


  def save_todo_data(self, title, content):
    todo = {
        'id': datetime.now(),
        'title': title,
        'content': content
    }
    self.todos.append(todo)


  def list_todos(self):
    count = 1
    print(f"\n {variables.log_list_todos}")

    for todo in self.todos:
        print(f"{count}) {todo['title']} --> {todo['content']}")
        count += 1

todo = Todo()

if (len(sys.argv) > 1):
    todo.list_todos()
else:
    todo.get_data_from_user()
    todo.list_todos()
