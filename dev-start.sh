docker build -t fastapi-demo-dev:latest .
docker run -it --mount type=bind,src=.,dst=/home/dev --network host -p 8000:8000 fastapi-demo-dev:latest /bin/sh
