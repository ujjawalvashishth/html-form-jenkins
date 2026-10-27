pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Check Python') {
            steps {
                bat 'python --version'
            }
        }

        stage('Test HTML Form') {
            steps {
                bat 'python -m unittest -v test_form.py'
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: All HTML form tests passed!'
        }

        failure {
            echo 'FAILURE: Check the console output for errors.'
        }
    }
}
