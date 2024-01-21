from pydantic import BaseModel, Field
from typing import List, Optional
from bson import ObjectId


class Difficulty(BaseModel):
    total: int
    solved: int
    beatsPercentage: Optional[float] = Field(default=None)


class Badge(BaseModel):
    name: str


class ContestRanking(BaseModel):
    attendedContestsCount: int
    rating: float
    globalRanking: int
    totalParticipants: int
    topPercentage: float
    badge: Badge


class LanguageStats(BaseModel):
    languageName: str
    problemsSolved: int


class Stat(BaseModel):
    name: str
    rank: int
    avatar: str
    totalProblems: int
    totalSolved: int
    easy: Difficulty
    medium: Difficulty
    hard: Difficulty
    contestRanking: Optional[ContestRanking] = Field(default=None)
    languageStats: List[LanguageStats]
