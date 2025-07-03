FROM python:3-alpine
WORKDIR /home/dev
COPY requirements.txt ./
RUN python -m pip install -r requirements.txt
EXPOSE 8000
COPY src/fastapi_demo/. .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]