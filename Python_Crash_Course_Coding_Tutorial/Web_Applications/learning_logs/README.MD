## Learning logs Sample Site

# Launch Dev site:
- step 1: launch Virtual Environment: 
```console
learning_log$ source 11_env/bin/activate
```
- step 2: Run the Server
```console
(11_env)learning_log$ python manage.py runserver
``` 
- step 3 enter in local address for site:
  - http://127.0.0.1:8000/admin/
  - http://127.0.0.1:8000/

# Entering the Django Interactive Shell of testing purposes
- be sure Virtual ENV is active
- Start the shell
```console
(11_env)learning_log$ python manage.py shell
``` 
- import a Model, in this case Topic:
```console
>>> from learning_logs.models import Topic
``` 
- get all of the instances of the model:
```console
>>> Topic.objects.all()
``` 
- obtain the current entries relative to a certain topic:
```console
>>> t=Topic.objects.get(id = 1)
>>> t.entry_set.all()
``` 
- obtain the text anddata added for a topic
```console
>>> t.text
>>> t.data_added
``` 
