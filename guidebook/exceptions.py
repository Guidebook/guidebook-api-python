class GuidebookError(Exception):
    """Base exception class"""
    pass


class BadRequestError(GuidebookError):
    """Raised when the guidebook API 400s"""
    pass


class AuthenticationError(GuidebookError):
    """Raised when the guidebook API 401s"""
    pass


class PermissionError(GuidebookError):
    """Raised when the guidebook API 403s"""
    pass


class RateLimitError(GuidebookError):
    """Raised when the guidebook API 429s"""
    pass
