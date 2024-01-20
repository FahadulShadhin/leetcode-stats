from fastapi import APIRouter
from services.LeetCodeService import LeetCodeGraphQLClient
from services.StatsService import StatsService

router = APIRouter()


@router.get('/')
def root():
    return {'message': 'Hello LeetCode Stats!'}


@router.get('/{leetcode_username}')
def get_user_stats(leetcode_username: str):
    leetcoce_client = LeetCodeGraphQLClient()
    problem_solved_stats = leetcoce_client.problems_solved(leetcode_username)
    language_stats = leetcoce_client.language_stats(leetcode_username)
    profile_stats = leetcoce_client.public_profile(leetcode_username)
    contest_ranking_stats = leetcoce_client.contest_ranking(leetcode_username)

    stats_service = StatsService(leetcode_username, problem_solved_stats,
                                 language_stats, profile_stats, contest_ranking_stats)

    stats = stats_service.construct_user_stats()

    return stats
