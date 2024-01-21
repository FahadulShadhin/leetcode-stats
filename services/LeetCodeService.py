import requests
import os
from dotenv import load_dotenv
from config.variables import Variables


class LeetCodeGraphQLClient:
    def __init__(self):
        load_dotenv()
        self.variables = Variables()
        self.url = self.variables.leetCodeGraphqlEndpoint

    def send_graphql_request(self, query: str, variables: dict):
        return requests.post(self.url, json={'query': query, 'variables': variables})

    def problems_solved(self, leetcode_username: str) -> dict:
        query = '''
        query userProblemsSolved($username: String!) {
            allQuestionsCount {
                difficulty
                count
            }
            matchedUser(username: $username) {
                problemsSolvedBeatsStats {
                    difficulty
                    percentage
                }
                submitStatsGlobal {
                    acSubmissionNum {
                        difficulty
                        count
                    }
                }
            }
        }
        '''
        variables = {'username': leetcode_username}

        try:
            response = self.send_graphql_request(query, variables)
            return response.json()
        except requests.exceptions.JSONDecodeError:
            return None

    def language_stats(self, leetcode_username: str) -> dict:
        query = '''
        query languageStats($username: String!) {
            matchedUser(username: $username) {
                languageProblemCount {
                    languageName
                    problemsSolved
                }
            }
        }
        '''
        variables = {'username': leetcode_username}

        try:
            response = self.send_graphql_request(query, variables)
            return response.json()
        except requests.exceptions.JSONDecodeError:
            return None

    def public_profile(self, leetcode_username: str) -> dict:
        query = '''
        query userPublicProfile($username: String!) {
            matchedUser(username: $username) {
                profile {
                    ranking
                    userAvatar
                    realName
                }
            }
        }
        '''
        variables = {'username': leetcode_username}

        try:
            response = self.send_graphql_request(query, variables)
            return response.json()
        except requests.exceptions.JSONDecodeError:
            return None

    def contest_ranking(self, leetcode_username: str) -> dict:
        query = '''
        query userContestRankingInfo($username: String!) {
            userContestRanking(username: $username) {
                attendedContestsCount
                rating
                globalRanking
                totalParticipants
                topPercentage
                badge {
                    name
                }
            }
        }
        '''
        variables = {'username': leetcode_username}

        try:
            response = self.send_graphql_request(query, variables)
            return response.json()
        except requests.exceptions.JSONDecodeError:
            return None
