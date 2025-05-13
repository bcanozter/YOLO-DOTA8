FROM ubuntu:jammy


WORKDIR /root

# Install dependencies
RUN apt-get update \
    && apt-get -y --quiet --no-install-recommends install \
    gcc \
    git \
    python3 \
    python3-pip \
    ffmpeg \
    libsm6 \
    libxext6

COPY . ${WORKDIR}/YOLO-DOTA8
RUN pip3 install -r ${WORKDIR}/YOLO-DOTA8/src/requirements.txt

# Run a default command, e.g., starting a bash shell
CMD ["bash"]