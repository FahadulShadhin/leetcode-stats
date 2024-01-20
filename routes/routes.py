from fastapi import APIRouter
from controllers.main import get_user_stats_controller

router = APIRouter()


@router.get('/')
def root():
    return {'message': 'Hello LeetCode Stats!'}


@router.get('/{leetcode_username}')
def get_user_stats(leetcode_username: str):
    return get_user_stats_controller(leetcode_username)
