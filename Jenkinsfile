pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                checkout([$class: 'GitSCM',
                    branches: [[name: 'main']],
                    userRemoteConfigs: [[
                        url: 'https://github.com/<your-username>/<your-repo>.git',
                        credentialsId: 'github_cred'
                    ]]
                ])
            }
        }

        stage('Install Dependencies') {
            steps {
                bat """
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                """
            }
        }

        stage('Run PyTest') {
            steps {
                bat """
                    pytest -v --html=report.html
                """
            }
        }

        stage('Archive Report') {
            steps {
                archiveArtifacts artifacts: 'report.html', fingerprint: true
            }
        }
    }
}
