ARG BASE_IMAGE=dahanna/python-alpine-package:alpine-python3-dev-git
# This Dockerfile has a default BASE_IMAGE, but you can override it with --build-arg.

# To be used in the FROM, naturally an ARG must come before the FROM.
# However, any *other* ARG above the FROM will be silently ignored.
# So it's very important that the ARGs are below the FROM.
FROM $BASE_IMAGE
ARG ETC_ENVIRONMENT_LOCATION

# .dockerignore keeps .tox and so forth out of the COPY
COPY dockerfiles/before_script.sh .
# The before_script.sh script sets several environment variables.
# Environment variables do *not* persist across Docker RUN lines.
# See also https://vsupalov.com/set-dynamic-environment-variable-during-docker-image-build/
COPY . {{cookiecutter.repo_name}}
RUN SSH_PRIVATE_DEPLOY_KEY=$FTP_PROXY . ./before_script.sh \
    && wget http://www.google.com/index.html && echo "wget works" && rm index.html \
    && pip install --no-cache-dir ./{{cookiecutter.repo_name}} \
    && (ssh-add -D || echo "ssh-add -D failed, hopefully because we never installed openssh-client in the first place.")

