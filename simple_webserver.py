from flask import Flask

# Flask 애플리케이션을 생성합니다.
app = Flask(__name__)

# 루트 경로에 대한 요청에 대한 응답을 처리합니다.
@app.route('/')
def hello():
    return 'Hello, World! This is a simple web server.'

# 웹 서버를 실행합니다.
if __name__ == '__main__':
    app.run(debug=True)
