FROM node:18-bullseye

# Update
RUN apt update

# Install pip
RUN apt install -y python3-pip

# Install request, pandas and openpyxl
RUN pip3 install requests pandas openpyxl