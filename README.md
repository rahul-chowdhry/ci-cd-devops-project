# Automated CI/CD DevOps Pipeline

## Project Title
Automated CI/CD Pipeline Using GitHub Actions,
Python Flask, Pytest and Docker.

## Technologies
- Python Flask
- Git and GitHub
- GitHub Actions
- Pytest
- Docker

## Features
- Automated testing
- Continuous Integration
- Application build preparation
- GitHub workflow automation

## Run Locally

Install dependencies:

pip install -r requirements.txt

Run application:

python app.py

Run tests:

python -m pytest -v

## Application URL

http://127.0.0.1:5000/

## Health Check

http://127.0.0.1:5000/health

## Pipeline Architecture

Developer -> Git Push -> GitHub
-> GitHub Actions -> Install Dependencies
-> Build -> Pytest -> Pipeline Success