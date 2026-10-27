pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Check HTML File') {
            steps {
                script {
                    if (!fileExists('index.html')) {
                        error('FAIL: index.html not found')
                    }
                }
                echo 'PASS: index.html exists'
            }
        }

        stage('Automated Form Tests') {
            steps {
                script {
                    def html = readFile('index.html')

                    def checks = [
                        'Form element': /<form\b/,
                        'Name field': /id="name"/,
                        'Email field': /type="email"/,
                        'Contact field': /id="contact"/,
                        'Submit button': /type="submit"/
                    ]

                    checks.each { label, pattern ->
                        if (!(html =~ pattern).find()) {
                            error("FAIL: ${label} missing")
                        }
                        echo "PASS: ${label} verified"
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'ALL TESTS PASSED!'
        }
        failure {
            echo 'PIPELINE FAILED. CHECK CONSOLE OUTPUT.'
        }
    }
}
