FROM python:3.8

WORKDIR /code

RUN wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz && \
    tar xzvf ta-lib-0.4.0-src.tar.gz && \
    cd ta-lib && \
    ./configure --prefix=/usr && \
    make && \
    make install && \
    cd .. && \
    rm -rf ta-lib*

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 80

ENV FLASK_APP=app.py
ENV FLASK_ENV=production
ENV FLASK_RUN_PORT=80
ENV SECRET_KEY="stockpilot"
ENV MONGO_URL_GENERAL=mongodb+srv://SEPU02:general123@sepcluster.yjn4m.mongodb.net/test_sep?retryWrites=true&w=majority
ENV MONGO_URL_ADMIN=mongodb+srv://SEPU01:User123@sepcluster.yjn4m.mongodb.net/test_sep?retryWrites=true&w=majority

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]