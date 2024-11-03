FROM python:3.13 
#I'm gona use the 3.13 python version


#to
WORKDIR /api 

#from
COPY . /api 

RUN pip install --no-cache-dir --upgrade -r /api/requirements.txt

#port
EXPOSE 5000 

CMD ["flask", "run"]
