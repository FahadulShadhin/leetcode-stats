class StatsService:
    def __init__(self, leetcode_username: str, problem_solved_stats: dict, language_stats: dict, profile_stats: dict, contest_ranking_stats: dict):
        self.username = leetcode_username
        self.problem_solved_stats = problem_solved_stats['data']
        self.language_stats = language_stats['data']
        self.profile_stats = profile_stats['data']
        self.contest_ranking_stats = contest_ranking_stats['data']

    def construct_user_stats(self):
        return {
            'username': self.username,
            'problems_solved': self.problem_solved_stats,
            'languages': self.language_stats,
            'profile': self.profile_stats,
            'contests': self.contest_ranking_stats
        }
