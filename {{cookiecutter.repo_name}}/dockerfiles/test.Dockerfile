ARG BASE_IMAGE
ARG ETC_ENVIRONMENT_LOCATION
FROM $BASE_IMAGE

# .dockerignore keeps .tox and so forth out of the COPY
COPY dockerfiles/before_script.sh .
RUN . ./before_script.sh
RUN wget http://www.google.com/index.html && echo "wget works" && rm index.html
COPY . {{cookiecutter.repo_name}}
RUN pip install --no-cache-dir ./{{cookiecutter.repo_name}}

