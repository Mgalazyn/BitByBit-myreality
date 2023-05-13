# BitByBit-myreality
Answer for recruitement task. My reality implementation

Models with fulfill the requirements specified. 
- One One-to-many realtion between the 'Task' and 'User'
- One many-to-many fields between 'Work' and 'Task'
- Custom user model with type field 

Next step serving data:
- Endpoint of login for user, after passing correct credentails, redirecting him to user view set
- Every model have specified endpoint for viewing models and fields of them. 
- Private endpoint (only for superusers) to create entry with nested objects which is 'Work'
- private endpoint (only for owners) to update entry with nested objects.

# Documentation of api 
Added through rest_framework Swagger 
so going to: http://127.0.0.1:8000/api/docs/ after runing server
you can read about all endpoints fields
