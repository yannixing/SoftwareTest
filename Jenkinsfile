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
        
                sh '''
                #!/bin/bash
        
                # 创建虚拟环境（如果不存在）
                if [ ! -d "venv" ]; then
                    python3 -m venv venv
                fi
        
                # 激活虚拟环境
                source venv/bin/activate
        
                # 升级 pip
                pip install --upgrade pip
        
                # 安装依赖
                pip install pytest pytest-html
        
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
