install - ```pip install -r requirements.txt```  
start - ```python manage.py makemigrations && python manage.py migrate && python manage.py runserver```

get specific - ```curl -X GET  http://localhost:8000/polls/1/```  
create new - ```curl -X POST -d '{"name": "abc"}' http://localhost:8000/polls/```  
update - ```curl -X PUT -d '{"name": "abc"}' http://localhost:8000/polls/1/```  
get with some filters (limit, order_by, stars, name, views) ```curl -X GET  'http://localhost:8000/polls/?stars=0'```   
delete - ```curl -X DELETE  'http://localhost:8000/polls/1/'```
