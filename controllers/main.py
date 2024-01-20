from fastapi.responses import JSONResponse
from services.LeetCodeService import LeetCodeGraphQLClient
from services.StatsService import StatsService
from exceptions import GraphqlException


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
    except GraphqlException:
        return JSONResponse(
            content={'status': 'Internal Server Error',
                     'message': 'Something went wrong while fetching your stats!'},
            status_code=500
        )

    stats_service = StatsService(leetcode_username, problem_solved_stats,
                                 language_stats, profile_stats, contest_ranking_stats)

    stats = stats_service.construct_user_stats()

    return JSONResponse(
        content={'status': 'Success',
                 'message': f'{leetcode_username} found', 'data': stats},
        status_code=200
    )
