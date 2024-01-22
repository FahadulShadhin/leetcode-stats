from fastapi.responses import JSONResponse
from services.LeetCodeService import LeetCodeGraphQLClient
from services.StatsService import StatsService
from services.DBService import DBService
from exceptions import GraphqlException
from config.logger import logger_config
from utils import response

logger = logger_config()


def root_controller():
    return response(200,
                    'Success',
                    'Put your LeetCode username in the url to fetch the stats >> https://leetcode-stats-api.onrender.com/{USERNAME}'
                    )


def get_user_stats_controller(leetcode_username: str):

    db_operations_service = DBService(leetcode_username)
    existing_user_id = db_operations_service.user_esists_in_db()

    if existing_user_id:
        logger.info(
            f'Stats for user {leetcode_username} already exists in db!')
        try:
            stats = db_operations_service.get_stats_from_db()
            logger.info('Stats fetched successfully!')
            return response(200, 'Success', f'{leetcode_username} found', stats)
        except Exception as e:
            logger.error(e)
            return response(500, 'Internal Server Error', 'Something went wrong while fetching your stats!')

    leetcoce_client = LeetCodeGraphQLClient()

    try:
        problem_solved_stats = leetcoce_client.problems_solved(
            leetcode_username)
        language_stats = leetcoce_client.language_stats(leetcode_username)
        profile_stats = leetcoce_client.public_profile(leetcode_username)
        contest_ranking_stats = leetcoce_client.contest_ranking(
            leetcode_username)

        if (
            not problem_solved_stats or
            not language_stats or
            not profile_stats or
            not contest_ranking_stats
        ):
            raise GraphqlException('GraphQL response if None.')
    except GraphqlException as e:
        logger.error(e)
        return response(500, 'Internal Server Error', 'Something went wrong while fetching your stats!')

    stats_service = StatsService(leetcode_username, problem_solved_stats,
                                 language_stats, profile_stats, contest_ranking_stats)

    stats = stats_service.construct_user_stats()

    if not stats:
        logger.info(f'{leetcode_username} is invalid user')
        return response(404, 'Not found', f"{leetcode_username} doesn't exist!")

    new_stats = stats_service.user_stats_to_save()
    try:
        db_operations_service.save_stats_to_db(new_stats)
        logger.info(f'Stats for {leetcode_username} saved to db!')
    except Exception as e:
        logger.error(e)

    return response(200, 'Success', f'{leetcode_username} found', stats)
