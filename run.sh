#!/bin/bash
sudo systemctl start mongod
source venv/bin/activate
uvicorn main:app --reload
