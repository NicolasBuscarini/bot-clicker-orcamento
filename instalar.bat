@echo off
python -m pip install virtualenv
python -m virtualenv .venv
.venv\scripts\activate && pip install -r requirements.txt

