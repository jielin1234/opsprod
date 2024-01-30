
- How does it works?
The frontend is going to send HTTP requests to the backend, the backend is going to fetch all the db from the db in MongoDB, then MongoDB is going to send the data to fast API to the backend server, then the backend using axios technology will send their response to the React frontend.

- Requirements:
Python
NodeJS
MongoDB account

Guides:
Start by creating a backend server with [[FASTAPI]]
1. Create a folder that contain both backend and frontend folders.
2. In the backend folder, create a requirements.txt which is for dependencies(Fast API, [[Uvicorn]], [[Motor]])
![[Pasted image 20240130104651.png]]
3. Create a virtual env using pipenv and install the depencies
4.  Next, we will need 3 files(main.py, [[database.py]], [[model.py]])
5. 