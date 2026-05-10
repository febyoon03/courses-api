# Courses API · 수강기록 관리 API

## 프로젝트 소개
FastAPI를 이용해 수강기록을 관리하는 REST API 서버입니다.
JSON 파일 기반으로 데이터를 읽고 쓰는 구조로 구현되었습니다.

## 주요 기능
- `GET /courses` : 전체 수강기록 조회
- `POST /courses` : 새로운 수강기록 추가
- JSON 파일 기반 데이터 영구 저장
- 잘못된 요청에도 서버 안정적 동작 (pydantic 검증)

## 기술 스택
- Backend: FastAPI
- Validation: Pydantic
- Server: Uvicorn
- Data: JSON 파일

## 실행 방법
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

## 데이터 구조
```json
{
  "course_name": "오픈소스소프트웨어실습",
  "year": "2026",
  "semester": "1",
  "grade": "A+"
}
```
