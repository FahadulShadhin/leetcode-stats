from pydantic import BaseModel, Field
from typing import Any, Optional


class Difficulty(BaseModel):
    total: int
    solved: int
    beatsPercentage: Optional[float] = Field(default=None)


class Stat(BaseModel):
    username: str
    name: str
    rank: int
    avatar: str
    totalProblems: int
    totalSolved: int
    easy: Difficulty
    medium: Difficulty
    hard: Difficulty
    contestRanking: Optional[dict[str, Any]] = Field(default=None)
    languageStats: list[dict[str, Any]]
