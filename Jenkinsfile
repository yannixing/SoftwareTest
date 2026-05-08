pipeline {
    agent any
    
    stages {
        
        stage('Test') {
            steps {
                echo '运行 pytest 测试...'
        
                sh '''
                #!/bin/bash
                source test/bin/activate
                # 运行测试
                pytest test_demo.py --html=report.html --self-contained-html
                '''
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
