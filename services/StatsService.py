from schemas.stat import Stat, Difficulty
from config.db import DBConfig


class StatsService:
    def __init__(self, leetcode_username: str, problem_solved_stats: dict, language_stats: dict, profile_stats: dict, contest_ranking_stats: dict):
        self.db_config = DBConfig()
        self.username = leetcode_username
        self.problem_solved_stats = problem_solved_stats['data']
        self.language_stats = language_stats['data']
        self.profile_stats = profile_stats['data']
        self.contest_ranking_stats = contest_ranking_stats['data']

    def construct_user_stats(self) -> dict:

        if (
            not self.problem_solved_stats['matchedUser'] or
            not self.language_stats['matchedUser'] or
            not self.profile_stats['matchedUser']
        ):
            return None

        user_stats = {
            'name': self.profile_stats['matchedUser']['profile']['realName'],
            'rank': self.profile_stats['matchedUser']['profile']['ranking'],
            'avatar': self.profile_stats['matchedUser']['profile']['userAvatar'],
            'totalProblems': self.problem_solved_stats['allQuestionsCount'][0]['count'],
            'totalSolved': self.problem_solved_stats['matchedUser']['submitStatsGlobal']['acSubmissionNum'][0]['count'],
            'easy': {
                'total': self.problem_solved_stats['allQuestionsCount'][1]['count'],
                'solved': self.problem_solved_stats['matchedUser']['submitStatsGlobal']['acSubmissionNum'][1]['count'],
                'beatsPercentage': self.problem_solved_stats['matchedUser']['problemsSolvedBeatsStats'][0]['percentage']

            },
            'medium': {
                'total': self.problem_solved_stats['allQuestionsCount'][2]['count'],
                'solved': self.problem_solved_stats['matchedUser']['submitStatsGlobal']['acSubmissionNum'][2]['count'],
                'beatsPercentage': self.problem_solved_stats['matchedUser']['problemsSolvedBeatsStats'][1]['percentage']
            },
            'hard': {
                'total': self.problem_solved_stats['allQuestionsCount'][3]['count'],
                'solved': self.problem_solved_stats['matchedUser']['submitStatsGlobal']['acSubmissionNum'][3]['count'],
                'beatsPercentage': self.problem_solved_stats['matchedUser']['problemsSolvedBeatsStats'][2]['percentage']
            },
            'contestRanking': self.contest_ranking_stats['userContestRanking'],
            'languageStats': self.language_stats['matchedUser']['languageProblemCount'],
        }

        return user_stats

    def save_user_stats(self):
        collection = self.db_config.collection

        existing_stat = collection.find_one({'username': self.username})
        if existing_stat:
            print(f'{self.username} already exists in db!')
            return

        new_stats = Stat(
            username=self.username,
            name=self.profile_stats['matchedUser']['profile']['realName'],
            rank=self.profile_stats['matchedUser']['profile']['ranking'],
            avatar=self.profile_stats['matchedUser']['profile']['userAvatar'],
            totalProblems=self.problem_solved_stats['allQuestionsCount'][0]['count'],
            totalSolved=self.problem_solved_stats['matchedUser'][
                'submitStatsGlobal']['acSubmissionNum'][0]['count'],
            easy=Difficulty(
                total=self.problem_solved_stats['allQuestionsCount'][1]['count'],
                solved=self.problem_solved_stats['matchedUser']['submitStatsGlobal']['acSubmissionNum'][1]['count'],
                beatsPercentage=self.problem_solved_stats['matchedUser'][
                    'problemsSolvedBeatsStats'][0]['percentage']
            ),
            medium=Difficulty(
                total=self.problem_solved_stats['allQuestionsCount'][2]['count'],
                solved=self.problem_solved_stats['matchedUser']['submitStatsGlobal']['acSubmissionNum'][2]['count'],
                beatsPercentage=self.problem_solved_stats['matchedUser'][
                    'problemsSolvedBeatsStats'][1]['percentage']
            ),
            hard=Difficulty(
                total=self.problem_solved_stats['allQuestionsCount'][3]['count'],
                solved=self.problem_solved_stats['matchedUser']['submitStatsGlobal']['acSubmissionNum'][3]['count'],
                beatsPercentage=self.problem_solved_stats['matchedUser'][
                    'problemsSolvedBeatsStats'][2]['percentage']
            ),
            contestRanking=self.contest_ranking_stats['userContestRanking'],
            languageStats=self.language_stats['matchedUser']['languageProblemCount'],
        )

        try:
            new_stats_dict = new_stats.dict()
            result = collection.insert_one(new_stats_dict)
            print(f'User stats for {self.username} saved to db!')
        except Exception as e:
            print(e)
