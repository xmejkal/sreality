FROM --platform=linux/amd64 python:3.10-alpine
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
ENTRYPOINT [ "flask" ]
CMD ["run", "--host=0.0.0.0", "--port=5115"]

#port 5000 is apparently taken by Airplay server on my Mac OS Ventura, so let's go with 5001
EXPOSE 5115 
