# Use an official Python image as the base image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    libffi-dev \
    libssl-dev \
    libjpeg-dev \
    zlib1g-dev \
    gcc \
    make \
    && rm -rf /var/lib/apt/lists/*

# Set the timezone to Europe/Vilnius
ENV TZ=Europe/Vilnius

# Set up the user for vscode
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME

# Switch to the vscode user
USER $USERNAME

# Set the working directory
WORKDIR /home/vscode

# Expose the default Home Assistant port
EXPOSE 8123
