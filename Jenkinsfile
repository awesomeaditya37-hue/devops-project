pipeline { 
    agent any
    
    stages {
        stage('checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install dependencies') {
            steps {
                sh '''
		python3 -m venv venv
		. venv/bin/activate
		pip install --upgrade pip
		pip install -r requirements.txt
		'''
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }
	stage('Docker image creation') {
	    steps {
		sh 'docker build -t flask-devops:${Build_Number} .'
	    }
        }
    post {
        success {
            echo 'Pipeline Successful'
        }
        failure {
            echo 'Pipeline failed'
        }
        always {
            cleanWs()
        }
    }

}
