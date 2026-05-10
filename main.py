from fastapi import FastAPI
from pydantic import BaseModel
import json
import logging

# ── 로깅 설정 ─────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Courses API",
    description="수강기록 관리 API",
    version="1.0.0"
)

# ── 데이터 모델 ───────────────────────────────────────────
class Course(BaseModel):
    course_name: str
    year: str
    semester: str
    grade: str

# ── 데이터 파일 경로 ──────────────────────────────────────
DATA_FILE = "courses.json"

def load_courses():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_courses(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# ── 엔드포인트 ────────────────────────────────────────────
@app.get("/courses")
def get_courses():
    logger.info("GET /courses requested")
    courses = load_courses()
    logger.info(f"Returning {len(courses)} courses")
    return courses

@app.post("/courses")
def add_course(course: Course):
    logger.info(f"POST /courses | course_name={course.course_name} | year={course.year}")
    courses = load_courses()
    courses.append(course.dict())
    save_courses(courses)
    logger.info(f"Course added. Total: {len(courses)}")
    return {"msg": "Course added successfully", "course": course}