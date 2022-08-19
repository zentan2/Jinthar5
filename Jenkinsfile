pipeline {
  agent any
 
  stages {

    stage('Build and run container') {
      steps {
        sh "docker stop j5app || echo 'App not running'"
        sh "docker container rm j5app || echo 'No container to remove'"
        sh "docker rmi j5/app:latest || echo 'No image to remove'"
        sh "docker build -t j5/app ."
        sh "docker run -d -p 8081:8090 --name j5app j5/app"
      }
    }
  }
}