pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo 'Source code checked out successfully.'
            }
        }

        stage('Check Python') {
            steps {
                bat '"C:\\Users\\hp\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" --version'
            }
        }

        stage('Test HTML Form') {
            steps {
                bat '"C:\\Users\\hp\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m unittest -v test_form.py'
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: All HTML form tests passed!'
        }
        failure {
            echo 'FAILURE: Check the Console Output for errors.'
        }
        always {
            echo 'Pipeline execution completed.'
        }
    }
}