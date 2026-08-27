pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                bat 'python -m py_compile src/calculator.py'
            }
        }

        stage('Test') {
            steps {
                bat 'python -m pip install pytest'
                bat 'python -m pytest'
            }
        }

        stage('Result') {
            steps {
                echo 'Build and tests completed successfully.'
            }
        }
    }
}