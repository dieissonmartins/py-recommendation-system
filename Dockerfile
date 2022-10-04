FROM python:3.10

WORKDIR /usr/src/app

#RUN pip3 install virtualenv
#RUN virtualenv /var/app
#RUN /var/app/bin/pip install --download-cache /src uwsgi

RUN pip3 install --upgrade pip3
RUN pip3 install pandas
RUN pip3 install numpy
RUN pip3 install matplotlib
RUN pip3 install seaborn
RUN pip3 install plotly

CMD ["python3"]