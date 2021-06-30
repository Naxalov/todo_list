# This project is a todo list

**The work to be done in this project will be indicated**

## **Install:**

`pip install django`

## TODO LIST
### Property:
- id(*int*): New task ID
- status(*bool*): True if done, otherwise False
- taskname(*str*): The name of the task
- description(*str*): The description of the task

### Methods:
- add
- update
- update_status
- get_all
- remove

# API:
## ADD
this is an api that adds a new task
- URL
    add/

- Method
    GET

- URL Params
    ### Required:
        id(int): New task ID
        taskname(str): The name of the task
    ### Optional:
        status(bool): True if done, otherwise False
        description(str): The description of the task

- Success Response:
    ### Code: 200
    ### Content: { id : 12 }
