pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                echo '从 GitHub 拉取代码...'
                git branch: 'main', url: 'https://github.com/yannixing/SoftwareTest.git'
            }
        }
        
        stage('Test') {
            steps {
                echo '运行 pytest 测试...'
                sh 'pip install pytest pytest-html'
                sh 'pytest test_demo.py --html=report.html --self-contained-html'
            }
        }
        
        stage('Result') {
            steps {
                echo '测试完成！'
            }
        }
    }
    
    post {
        always {
            echo '无论成功还是失败，都会执行这一步。'
        }
    }
}
