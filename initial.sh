#!/bin/sh
sudo rm -rf mysql/data_dir/*

sudo docker-compose build
sudo docker-compose up -d
