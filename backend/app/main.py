from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import chat

app = FastAPI(
    title="Chat API",
    description="간단한 채팅 API 서버 - PR 테스트용 수정",
    version="1.0.1"
)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록
app.include_router(chat.router)


@app.get("/")
async def root():
    """루트 엔드포인트"""
    # 의도적인 버그 1: 문법 오류 (닫히지 않은 괄호)
    return {"message": "Chat API Server", "test": "PR 테스트 완료!", "status": "running"


@app.get("/health")
async def health_check():
    """헬스체크 엔드포인트"""
    return {"status": undefined_variable} 