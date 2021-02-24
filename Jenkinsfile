pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        git(url: 'https://github.com/brounea/project1.git', branch: 'master', poll: true)
      }
    }

  }
}