# https://github.com/tensorflow/tensorflow/tree/master/tensorflow/tools/dockerfiles
# https://github.com/tensorflow/tensorflow/blob/master/tensorflow/tools/dockerfiles/assembler.py
# https://github.com/tensorflow/community/blob/master/rfcs/20180731-dockerfile-assembler.md

# We eventually want to assemble Dockerfiles from partials like TensorFlow.
# But we aren't doing that yet.
# This is just a tiny starting point that assembles a script file to be run in each Dockerfile.

import os.path
import yaml

if __name__ == "__main__":
    yml = yaml.safe_load(open('.before_script.yml'))
    with open(os.path.join('dockerfiles', 'before_script.sh'), 'w') as scriptFile:
        for line in yml['default']['before_script']:
            print(line, file=scriptFile)
