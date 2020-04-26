FROM python:3.8.2

RUN mkdir -p /usr/src/app/


WORKDIR /usr/src/app/

COPY . /usr/src/app/

RUN pip install -r requirements.txt

RUN chmod +x /usr/src/app/plot_and_push.sh
# CMD [ "python", "app.py" ]
CMD [ "./plot_and_push.sh" ]