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

## **Add method**
----
	Return json data about added task.

- **URL**_
	/add

- **Method:**_
  `GET`

- **URL Params**_
  **Required:**_
  `status(bool)`
  `taskname(str)`
  `description(str)` 

- **Success Response:**_

  - **Code:** 200_
    **Content:**
           `{ 
              status : False,
              taskname : "taskname", 
              description : "description"
            }`
 
- **Error Response:**_

  - **Code:** 404 NOT FOUND
    **Content:**_
           `{ 
              error : "eror description" 
            }`