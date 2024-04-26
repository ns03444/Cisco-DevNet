Notes on work computer

Deploying Flask App in Dockerfile

Dockerfile work just like shell script - a series of commands

Dockerfile installs necessary software to/min requirements to contruct the container/run the app

FROM - Tell it what OS it needs to get its OS from (use)

When docker goes to build the container its going ubuntu18.04 image as base OS

RUN - runs known OS commands

CMD - runs raw commands

COPY - copies local files to the container

WORKDIR - tell container what directory is base dir

Pip3 install

make sure its up-to-date & python is installed

ENTRYPOINT - what program we want to enter/execute python3

Docker build - builds the actual container

Docker run - runs the container after it has been built locally

-p - port forwarding - run as many instances of a container as you want on a machine as long as giving different ports