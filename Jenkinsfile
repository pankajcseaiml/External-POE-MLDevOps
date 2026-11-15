pipeline {
    agent any

    environment {
        PYTHON = 'python'
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Checking out code from Git...'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing required Python packages...'
                bat '%PYTHON% -m pip install --upgrade pip'
                bat '%PYTHON% -m pip install -r requirements.txt'
            }
        }

        stage('Run Pytest') {
            steps {
                echo 'Running Pytest test suite for Addition, Subtraction, Multiplication, Division...'
                bat '%PYTHON% -m pytest -p no:dash -v tests/'
            }
        }

        stage('Evidently Tool Monitoring') {
            steps {
                echo 'Running Evidently AI data drift monitoring...'
                bat '%PYTHON% evidently_monitor.py'
            }
        }

        stage('MLflow Tracking') {
            steps {
                echo 'Logging arithmetic runs to MLflow...'
                bat '%PYTHON% train_and_track_mlflow.py'
            }
        }

        stage('Docker Build and Run') {
            steps {
                echo 'Building and running Docker container...'
                bat 'docker build -t arithmetic-app:latest .'
                bat 'docker run --rm arithmetic-app:latest'
            }
        }
    }

    post {
        always {
            echo 'Jenkins pipeline completed.'
        }
        success {
            echo 'Arithmetic Operations CI/CD Pipeline passed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check stage logs above.'
        }
    }
}
