FROM python:3-alpine
WORKDIR /home/dev
COPY requirements.txt ./
RUN python -m pip install -r requirements.txt
EXPOSE 8000
COPY . .
CMD ["fastapi", "run", "src/fastapi_demo/main.py"]