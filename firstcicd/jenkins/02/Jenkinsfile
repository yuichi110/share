pipeline {
  agent any
  stages {
    stage('Pre Check') {
      steps {
        sh "python3 --version"
        sh "python3 -c 'import flask'"
      }
    }
    stage('Cleanup') {
      steps {
        echo "stop background flask job"
        sh "sudo kill `pgrep python3` || true"
      }
    }
    stage('Deploy') {
      steps {
        echo "start flask as background job"
        sh "sudo nohup python3 server.py >> log.txt 2>&1 &"
      }
    }
  }
}