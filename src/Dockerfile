FROM python:3.8

#docker build -t [imageName]
#docker run -d --name [containerName] -p 80:[port] [imageName]


#Is this even required?
COPY . .

RUN pip install -r requirements.txt

EXPOSE 80

WORKDIR "/modules"

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]