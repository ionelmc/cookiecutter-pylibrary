ARG BASE_IMAGE
ARG HTTP_PROXY
ARG HTTPS_PROXY
ARG NO_PROXY
FROM $BASE_IMAGE

ENV http_proxy=$HTTP_PROXY
ENV https_proxy=$HTTPS_PROXY
ENV no_proxy=$NO_PROXY

# .dockerignore applies to COPY
COPY . {{cookiecutter.repo_name}}
RUN ls && pip install --no-cache-dir ./{{cookiecutter.repo_name}}

