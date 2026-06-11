pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main',
                url: 'https://github.com/raveeshajoshi7/Employee-Management-App.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t employee-app:latest .'
            }
        }

        stage('Deploy Container') {
            steps {
                bat 'docker stop employee-app || exit 0'
                bat 'docker rm employee-app || exit 0'
                bat 'docker run -d --name employee-app -p 5000:5000 employee-app:latest'
            }
        }
    }
}