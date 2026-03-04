from config import endpoints

class AuthAPI:
    def __init__(self, api_context):
        self.api = api_context

    def register(self, payload: dict):
        return self.api.post(endpoints.REGISTER, data=payload)

    def login(self, email: str, password: str):
        return self.api.post(endpoints.LOGIN, data={
            "email": email,
            "password": password
        })

    def logout(self, token: str):
        return self.api.delete(endpoints.LOGOUT, headers={
            "Authorization": f"Bearer {token}"
        })

    def refetch_token(self, token: str):
        return self.api.post(endpoints.REFETCH_TOKEN, headers={
            "Authorization": f"Bearer {token}"
        })
