# flask-container-app
This is a simple flask application. 
This application is packaged into a docker iamge and run as a docker container. 

The End user needs to pull the source code from this repository which also has the dockerfile. 

Perform following steps in order to run the application container

1. git clone https://github.com/pankaj120181/flask-container-app.git
2. cd flask-container-app
3. Build the docker images using following command from the workspace containing dockerfile. 
   **docker build -t flask-app:v1.0 .**
2. After image is built, run following command, 
   **docker run  -d -p 80:5000 flask-app:v2.0**
3. Browse the application as http://127.0.0.1/
   **Note: Make sure no other application is running on port 80 on the local host**
  
