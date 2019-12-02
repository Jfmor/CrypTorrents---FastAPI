FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

#docker build -t [imageName]
#docker run -d --name [containerName] -p 80:[port] [imageName]


#Is this even required?
COPY . .

RUN pip install -r requirements.txt

#might need to comment this out
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "$PORT"]