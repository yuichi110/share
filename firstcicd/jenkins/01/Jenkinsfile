pipeline {
  agent any
  stages {
    stage('Pre Check') {
      steps {
        sh "python3 --version"
        sh "python3 -c 'import flask'"
      }
    }
  }
}