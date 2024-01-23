from fastapi import APIRouter
from controllers.main import get_user_stats_controller, root_controller

router = APIRouter()


@router.get('/')
def root():
    return root_controller()


@router.get('/{leetcode_username}')
def get_user_stats(leetcode_username: str):
    return get_user_stats_controller(leetcode_username)
