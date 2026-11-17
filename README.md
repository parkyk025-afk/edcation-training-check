# 직원 교육이수 조회 시스템 — 시험용

**주의: 가상 데이터만 포함된 시연용 웹사이트입니다.** 이름+사번만으로 조회하는 것은 본인 인증이 아니므로 실제 직원 개인정보나 이수 내역을 이 앱에 넣으면 안 됩니다.

## GitHub 업로드

이 ZIP 파일을 압축 해제하고, 폴더 안의 `app.py`, `requirements.txt`, `render.yaml`, `.gitignore`, `README.md`, `templates` 폴더를 GitHub 저장소의 **Add file → Upload files**로 올린 뒤 **Commit changes**를 누르세요. ZIP 자체를 업로드하지 마세요.

## Render 배포

1. https://dashboard.render.com 에 GitHub 계정으로 로그인
2. **New → Web Service** 선택 후 GitHub 저장소 `education-training-check` 연결
3. Runtime: **Python**, Build Command: `pip install -r requirements.txt`, Start Command: `gunicorn --bind 0.0.0.0:$PORT app:app` 선택
4. 이용 가능한 요금제 선택 (무료 옵션 제공 여부는 Render 화면에서 확인)
5. **Deploy Web Service** 클릭 후 생성된 `https://...onrender.com` 주소 접속

시험 계정: `홍길동 / 2026001`, `김하늘 / 2026002`.

## 실제 운영 전 필수 사항

- 대학 정보전산원과 협의해 SSO(OIDC 또는 SAML) 연동, 로그인 사용자 식별자와 사번의 서버 측 매핑 적용
- 실데이터는 GitHub에 업로드하지 말고 접근통제된 데이터베이스에 보관
- HTTPS, 조회 권한 제한, 접근 기록, 보존기간, 개인정보 처리 검토 및 보안 점검
- Render의 운영 리전, 데이터 처리 및 기관 보안 규정 적합성 확인

실데이터 업로드·관리 기능은 의도적으로 구현하지 않았습니다.
