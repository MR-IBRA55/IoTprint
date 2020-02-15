[![Build Status](https://travis-ci.org/Captain-IR/IoTprint.svg?branch=master)](https://travis-ci.org/Captain-IR/IoTprint)
# IoTprint
Bring your 3D printer online and print your files remotely.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
See deployment for notes on how to deploy the project on a live system.

### Prerequisites
* Make sure you have an **Ubuntu** computer connected to the 3D printer with a **USB**.
* Download and install [Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
### Installation
**Warning:** no printing for now just test the web app and api.
```
git clone https://github.com/Captain-IR/IoTprint.git && cd IoTprint
sudo apt install docker-compose
docker compose up
Type 127.0.0.1 in your browser to access the home page
```
