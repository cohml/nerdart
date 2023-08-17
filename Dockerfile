FROM continuumio/miniconda3

ENV NERDART_ENV_DIR="/opt/env"
ENV NERDART_PKG_DIR="/opt/nerdart"

RUN mkdir $NERDART_PKG_DIR

WORKDIR $NERDART_PKG_DIR
COPY ./nerdart/ ./

WORKDIR /
COPY ./LICENSE ./
# copy + rename
COPY ./entrypoint.sh.docker ./entrypoint.sh

WORKDIR /home/root
# copy + rename
COPY ./.bashrc.docker ./.bashrc

WORKDIR /opt
COPY ./environment.yaml ./nerdart/ ./README.md ./setup.py ./

RUN set -e \
 && conda update -n base -c defaults conda \
 && conda env create --file ./environment.yaml --prefix $NERDART_ENV_DIR \
 && echo Conda environment successfully created

WORKDIR /
ENTRYPOINT ["bash", "entrypoint.sh"]
