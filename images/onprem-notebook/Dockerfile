# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
ARG REGISTRY=quay.io
ARG OWNER=jupyter
ARG BASE_CONTAINER=$REGISTRY/$OWNER/minimal-notebook
FROM $BASE_CONTAINER

LABEL maintainer="Jupyter Project <jupyter@googlegroups.com>"

# Fix: https://github.com/hadolint/hadolint/wiki/DL4006
# Fix: https://github.com/koalaman/shellcheck/wiki/SC3014
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER root

RUN apt-get update --yes && \
    apt-get install --yes --no-install-recommends \
    # for cython: https://cython.readthedocs.io/en/latest/src/quickstart/install.html
    build-essential \
    # for latex labels
    cm-super \
    dvipng \
    # for matplotlib anim
    ffmpeg && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

USER ${NB_UID}

# Install Python 3 packages
RUN mamba install --yes \
    'numpy' \
    'matplotlib-base' && \
    mamba clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

ENV UV_EXTRA_INDEX_URL="https://pypi.org/simple https://pypi.rtzr.ai/"
# COPY requirements.compiled.txt requirements.txt    
RUN pip install --no-cache-dir uv \
    && uv pip install --no-cache --system rtboost \
    && pip uninstall -y uv
# Install facets package which does not have a `pip` or `conda-forge` package at the moment
WORKDIR /tmp
RUN git clone https://github.com/PAIR-code/facets && \
    jupyter nbclassic-extension install facets/facets-dist/ --sys-prefix && \
    rm -rf /tmp/facets && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

# Import matplotlib the first time to build the font cache
RUN MPLBACKEND=Agg python -c "import matplotlib.pyplot" && \
    fix-permissions "/home/${NB_USER}"

USER ${NB_UID}

WORKDIR "${HOME}"
COPY __init__.py /home/jovyan/rtzr/__init__.py
