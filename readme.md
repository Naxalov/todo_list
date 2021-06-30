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

## - URL:
 *<add/>*

## -METHOD:
*GET|POST*

## - URL Params:
- id
- status
- taskname
- description

## - Required:
- id=[integer]
- taskname=[string]

## - Optional:
- status=[bool]
- description=[string]

## - Succes response:
** {'result': 'succesfully!'} **
