from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional


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
    contestRanking: Optional[Dict[str, Any]] = Field(default=None)
    languageStats: List[Dict[str, Any]]
