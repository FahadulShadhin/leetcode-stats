from fastapi import APIRouter

router = APIRouter()


@router.get('/')
def root():
    return {'message': 'Hello LeetCode Stats!'}


@router.get('/{leetcode_username}')
def get_user_stats(leetcode_username: str):
    return leetcode_username
