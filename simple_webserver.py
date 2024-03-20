from flask import Flask

# Flask 애플리케이션을 생성합니다.
app = Flask(__name__)

# 루트 경로에 대한 요청에 대한 응답을 처리합니다.
@app.route('/')
def hello():
    return 'Hello, World! This is a simple web server.'

# 웹 서버를 실행합니다. 호스트를 0.0.0.0으로 설정하여 외부에서 접속할 수 있도록 합니다.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
