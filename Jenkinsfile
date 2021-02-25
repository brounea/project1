pipeline {
  agent any
  stages {
    stage('checkout') {
      steps {
        script {
          properties([pipelineTriggers([pollSCM('* * * * *')])])
        }

        git 'https://github.com/brounea/project1.git'
      }
    }

    stage('Setup venv') {
      steps {
        script {
          sh 'python3.9 -m venv calculator'
          sh '.  calculator/bin/activate'
          sh 'pip3 install flask pymysql selenium'
        }

      }
    }

    stage('run RestApp') {
      steps {
        sh 'sh \' nohup python3.9 web_app.py &\''
      }
    }

  }
}