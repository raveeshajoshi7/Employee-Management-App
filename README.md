# Employee Management Application - CI/CD Pipeline Project

## Project Overview

This project demonstrates an end-to-end CI/CD pipeline using GitHub, Jenkins, Docker, and Python Flask. The application is a simple Employee Management Portal that displays employee information through a web interface.

The main objective of this project is to automate the build and deployment process using Jenkins and Docker whenever application code is updated in GitHub.

## Technologies Used

* Python Flask
* Docker
* Jenkins
* Git & GitHub
* Windows Environment

## Project Architecture

Developer → GitHub → Jenkins Pipeline → Docker Build → Docker Container Deployment

## Features

* Employee Management Web Application
* Containerized using Docker
* Source Code Management with GitHub
* Automated Build Process using Jenkins
* Automated Deployment using Docker Containers
* CI/CD Pipeline Implementation

## Docker Implementation

* Created a Dockerfile to containerize the Flask application.
* Built Docker images using Jenkins pipeline.
* Deployed application containers using Docker run commands.
* Exposed application on port 5000.

## Jenkins Pipeline

The Jenkins pipeline performs the following tasks:

1. Pulls latest source code from GitHub.
2. Builds Docker image.
3. Stops existing container.
4. Removes old container.
5. Deploys a new container with the latest code.

## Learning Outcomes

Through this project, I gained hands-on experience in:

* CI/CD Concepts
* Jenkins Pipeline Development
* Docker Image Creation
* Container Deployment
* GitHub Integration with Jenkins
* Troubleshooting Jenkins and Docker Issues
* Application Containerization

## Application Access

Application URL:

http://localhost:5000

## Future Enhancements

* Employee Registration Form
* Database Integration
* Automated GitHub Webhooks
* AWS EC2 Deployment
* Kubernetes Deployment
* Monitoring using Prometheus and Grafana
