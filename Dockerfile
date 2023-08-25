FROM alpine

COPY ./requirements /requirements
COPY ./scripts /scripts
COPY ./src /src

WORKDIR /src

EXPOSE 8000

RUN /py/bin/pip install -r /requirements/development.txt

RUN chmod -R +x /scripts && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    adduser --disabled-password --no-create-home djshop && \
    chown -R djshop:djshop /vol && \
    chmod -R 755 /vol

ENV PATH="/sripts:/py/bin:$PATH"

USER djshop

CMD [ "run.sh" ]