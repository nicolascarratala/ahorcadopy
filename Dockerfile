FROM python:3.8

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY requirements.txt .

RUN python -m venv venv

RUN ./venv/Scripts/activate

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY ./ .

CMD ["python", "main.py"]