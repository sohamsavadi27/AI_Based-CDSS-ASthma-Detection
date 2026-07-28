pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                // Replace with your actual GitHub repository URL
                git 'https://github.com/your-username/python-project.git'
            }
        }
        stage('Build') {
            steps {
                sh 'python3 --version'
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m unittest discover'
            }
        }
    }
    
    post {
        success {
            echo 'Build Successful!'
        }
        failure {
            echo 'Build Failed!'
        }
    }
}
