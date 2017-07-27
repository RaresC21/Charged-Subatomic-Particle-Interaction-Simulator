pipeline {
  agent any
  stages {
    stage('build') {
      steps {
      	sh 'pip install --no-cache-dir -r numpy'
      	sh 'pip install --no-cache-dir -r matplotlib'
      }
    }
    stage('run') {
      steps {
      	sh 'python simulator.py'
      }
    }
  }
}
