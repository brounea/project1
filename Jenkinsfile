pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        git(url: 'https://github.com/brounea/project1.git', branch: 'master', poll: true)
      }
    }

    stage('runRestServer') {
      steps {
        sh '''withPythonEnv(\'venv-prj1\') 
	// Creates the virtualenv before proceeding
	sh \'pip install nose\'

//sh \' python rest_app.py\'
'''
      }
    }

    stage('runServerTest') {
      steps {
        sh 'sh \' python rest_app.py\''
      }
    }

  }
}