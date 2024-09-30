#!/bin/sh

docker run -it --rm -p 10000:8888 -v "${PWD}":/home/jovyan/work onprem-notebook:dev


