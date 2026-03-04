from typing import Any, Dict, Optional

class BaseApi:
    def __init__(self, request_context):
        self.request = request_context
