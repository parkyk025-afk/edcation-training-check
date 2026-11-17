import os
import hmac
from flask import Flask, render_template, request

app = Flask(__name__)
# Demonstration-only fictitious records. Never store real staff data in source control.
DEMO = {
    ('홍길동', '2026001'): [
        {'course': '개인정보 보호 교육', 'date': '2026-03-12', 'hours': 2, 'status': '이수'},
        {'course': '정보보안 교육', 'date': '2026-05-20', 'hours': 1, 'status': '이수'},
    ],
    ('김하늘', '2026002'): [
        {'course': '직장 내 괴롭힘 예방교육', 'date': '2026-06-15', 'hours': 2, 'status': '이수'},
    ],
}

@app.get('/')
def index():
    return render_template('index.html', result=None, error=None)

@app.post('/lookup')
def lookup():
    name = request.form.get('name', '').strip()[:50]
    emp_id = request.form.get('employee_id', '').strip()[:30]
    if not name or not emp_id:
        return render_template('index.html', result=None, error='이름과 사번을 모두 입력해 주세요.'), 400
    # Explicitly restrict this unauthenticated example to fake data.
    result = next((v for (n, i), v in DEMO.items() if hmac.compare_digest(n, name) and hmac.compare_digest(i, emp_id)), None)
    return render_template('index.html', result=result, error=None if result else '일치하는 시험용 교육이수 내역이 없습니다.', name=name)

@app.get('/health')
def health():
    return {'status': 'ok'}

if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1', port=int(os.environ.get('PORT', '5000')))
