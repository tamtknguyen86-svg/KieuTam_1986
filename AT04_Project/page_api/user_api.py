from config import endpoints

class UserAPI:
    def __init__(self, api_context):
        self.api = api_context

    def me(self, token: str):
        return self.api.get(endpoints.ME, headers={
            "Authorization": f"Bearer {token}"
        })

    def patch_profile(self, token: str, email: str, name: str, phone: str, address: str):
        return self.api.patch(endpoints.PATCH_PROFILE,
            headers={"Authorization": f"Bearer {token}"},
            data={"email": email,
                "name": name,
                "phone": phone,
                "address": address
                }
        )
    
    def patch_password(self, token: str, email: str, password: str, password_old: str):
        return self.api.patch(endpoints.PATCH_PROFILE,
            headers={"Authorization": f"Bearer {token}"},
            data={"email": email,
                "password": password,
                "password_old": password_old
                }
        )