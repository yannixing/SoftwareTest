pipeline {
    agent any
    
    stages {
        
        stage('Test') {
            steps {
                echo '运行 pytest 测试...'
        
                sh '''
                #!/bin/bash
                set -e
        
                # 如果 test 虚拟环境不存在或损坏，则重新创建
                if [ ! -f "test/bin/activate" ]; then
                    rm -rf test
                    python3 -m venv test
                fi
        
                # 激活虚拟环境
                . test/bin/activate
        
                # 安装依赖
                python -m pip install --upgrade pip
                python -m pip install pytest pytest-html
        
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
