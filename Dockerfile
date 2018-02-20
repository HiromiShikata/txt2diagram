FROM alpine:latest

ENV NAME "defaultapname"

RUN mkdir /graphviz
RUN apk add --update graphviz ttf-dejavu
RUN apk add curl python py-pip jq vim
RUN pip install bottle

ADD ./app/webserver.py /app/webserver.py


RUN rm -rf /var/cache/apk/*


WORKDIR /graphviz

CMD ["sh", "-c", "python /app/webserver.py"]

EXPOSE 8500
