"""Data models and schemas."""

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Message:
    """Message schema."""
    
    role: str
    content: str


@dataclass
class AgentResponse:
    """Agent response schema."""
    
    response: str
    tools_used: List[str] = None
    confidence: float = 0.0
