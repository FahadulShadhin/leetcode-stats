from fastapi.responses import JSONResponse
from services.LeetCodeService import LeetCodeGraphQLClient
from services.StatsService import StatsService
from exceptions import GraphqlException
from config.logger import logger_config

logger = logger_config()


def root_controller():
    return JSONResponse(
        content={'status': 'Success',
                 'message': 'Put your LeetCode username in the url to grab the stats.',
                 'example': 'https://leetcode-stats-api.onrender.com/<YOUR_LEETCODE_USERNAME>'},
        status_code=200,
    )


def get_user_stats_controller(leetcode_username: str):
    leetcoce_client = LeetCodeGraphQLClient()

    try:
        problem_solved_stats = leetcoce_client.problems_solved(
            leetcode_username)
        language_stats = leetcoce_client.language_stats(leetcode_username)
        profile_stats = leetcoce_client.public_profile(leetcode_username)
        contest_ranking_stats = leetcoce_client.contest_ranking(
            leetcode_username)

        if not problem_solved_stats or not language_stats or not profile_stats or not contest_ranking_stats:
            raise GraphqlException('GraphQL response if None.')
    except GraphqlException as e:
        logger.error(e)
        return JSONResponse(
            content={'status': 'Internal Server Error',
                     'message': 'Something went wrong while fetching your stats!'},
            status_code=500
        )

    stats_service = StatsService(leetcode_username, problem_solved_stats,
                                 language_stats, profile_stats, contest_ranking_stats)

    stats = stats_service.construct_user_stats()

    if not stats:
        return JSONResponse(
            content={'status': 'Not found',
                     'message': f"{leetcode_username} doesn't exist!"},
            status_code=404,
        )

    stats_service.save_user_stats()

    return JSONResponse(
        content={'status': 'Success',
                 'message': f'{leetcode_username} found', 'data': stats},
        status_code=200
    )
