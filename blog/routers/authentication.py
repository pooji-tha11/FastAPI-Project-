from fastapi import FastAPI

router = APIRouter()

@router.post('/login')
def login():
    