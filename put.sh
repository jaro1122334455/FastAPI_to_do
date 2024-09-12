curl -X 'PUT' \
  'http://127.0.0.1:8000/tasks/0' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "Complete project",
  "description": "Update the FastAPI project with new features",
  "is_done": true
}'
