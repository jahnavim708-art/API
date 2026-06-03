class LMSException(Exception):
    """
    Base exception for all LMS custom exceptions.
    """

    def __init__(
        self,
        message: str = "Application error"
    ):
        self.message = message
        super().__init__(self.message)


class UserNotFoundException(LMSException):
    """
    Raised when a user is not found.
    """

    def __init__(
        self,
        message: str = "User not found"
    ):
        super().__init__(message)


class InvalidCredentialsException(LMSException):
    """
    Raised when login credentials are invalid.
    """

    def __init__(
        self,
        message: str = "Invalid username or password"
    ):
        super().__init__(message)


class UserAlreadyExistsException(LMSException):
    """
    Raised when username or email already exists.
    """

    def __init__(
        self,
        message: str = "User already exists"
    ):
        super().__init__(message)


class CourseNotFoundException(LMSException):
    """
    Raised when course is not found.
    """

    def __init__(
        self,
        message: str = "Course not found"
    ):
        super().__init__(message)


class EnrollmentNotFoundException(LMSException):
    """
    Raised when enrollment is not found.
    """

    def __init__(
        self,
        message: str = "Enrollment not found"
    ):
        super().__init__(message)


class LessonNotFoundException(LMSException):
    """
    Raised when lesson is not found.
    """

    def __init__(
        self,
        message: str = "Lesson not found"
    ):
        super().__init__(message)


class QuizNotFoundException(LMSException):
    """
    Raised when quiz is not found.
    """

    def __init__(
        self,
        message: str = "Quiz not found"
    ):
        super().__init__(message)


class AssignmentNotFoundException(LMSException):
    """
    Raised when assignment is not found.
    """

    def __init__(
        self,
        message: str = "Assignment not found"
    ):
        super().__init__(message)


class UnauthorizedException(LMSException):
    """
    Raised when user lacks permission.
    """

    def __init__(
        self,
        message: str = "Unauthorized access"
    ):
        super().__init__(message)


class ForbiddenException(LMSException):
    """
    Raised when user is forbidden from performing an action.
    """

    def __init__(
        self,
        message: str = "Access forbidden"
    ):
        super().__init__(message)


class ValidationException(LMSException):
    """
    Raised when business validation fails.
    """

    def __init__(
        self,
        message: str = "Validation failed"
    ):
        super().__init__(message)


class DatabaseException(LMSException):
    """
    Raised when a database operation fails.
    """

    def __init__(
        self,
        message: str = "Database operation failed"
    ):
        super().__init__(message)