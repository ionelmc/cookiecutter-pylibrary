ARG BASE_IMAGE=dahanna/python-alpine-package:alpine-python3-dev-git
# This Dockerfile has a default BASE_IMAGE, but you can override it with --build-arg.

# To be used in the FROM, naturally an ARG must come before the FROM.
# However, any *other* ARG above the FROM will be silently ignored.
# So it's very important that the ARGs are below the FROM.
# https://docs.docker.com/engine/reference/builder/#understand-how-arg-and-from-interact
FROM $BASE_IMAGE
ARG ETC_ENVIRONMENT_LOCATION

COPY dockerfiles/before_script.sh .

# .dockerignore keeps .tox and so forth out of the COPY.
COPY . {{cookiecutter.repo_name}}
# If we ran before_script in a separate RUN before the COPY of the code,
# then that layer could stay cached when the repo contents changed,
# but it's more valuable to keep all the environment variables confined to a single RUN.
# before_script.sh shouldn't take long to run anyway.

# The before_script.sh script sets several environment variables.
# Environment variables do *not* persist across Docker RUN lines.
# See also https://vsupalov.com/set-dynamic-environment-variable-during-docker-image-build/
RUN if [ -z ${FTP_PROXY+ABC} ]; then echo "FTP_PROXY is unset, so not doing any shenanigans."; else SETTER="SSH_PRIVATE_DEPLOY_KEY=${FTP_PROXY}"; fi \
    && ${SETTER} . ./before_script.sh \
    && wget http://www.google.com/index.html && echo "wget works" && rm index.html \
    && pip install --no-cache-dir ./{{cookiecutter.repo_name}} \
    && (ssh-add -D || echo "ssh-add -D failed, hopefully because we never installed openssh-client in the first place.")

# Ideally we want assembler.py to insert appropriate EXPOSE instructions for any ports,
# such as port 8888 for Jupyter or port 8050 for Plotly Dash.
# However, unless you're having containers talk to other containers,
# EXPOSE does not technically do anything you care about;
# docker run --publish does all the heavy lifting.
# https://www.ctl.io/developers/blog/post/docker-networking-rules
# https://we-are.bookmyshow.com/understanding-expose-in-dockerfile-266938b6a33d
# https://docs.docker.com/engine/reference/builder/#expose

CMD ["python", "-m", "{{cookiecutter.package_name}}"]

