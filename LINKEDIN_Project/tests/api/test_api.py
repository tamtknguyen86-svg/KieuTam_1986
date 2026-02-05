import pytest, requests
from page_api.user_api import UserAPI
from page_api.authentication_api import AuthAPI

# -------------------------
# Login API → lấy token
# -------------------------
def test_login_by_api_get_token(login_get_token):
    user_token = login_get_token
    print(f"User's Token : {user_token}")

# -------------------------
# GET /api/me
# -------------------------
def test_get_api_me(api_context, registered_user, login_get_token):
    token = login_get_token
    headers = {"Authorization": f"Bearer {token}"}

    user_api = UserAPI(api_context)
    me_resp = user_api.me(token)

    assert me_resp.status == 200, f"GET /api/me failed: {me_resp.status} - {me_resp.text()}"
    me_body = me_resp.json()

    assert me_body["email"] == registered_user["email"]
    assert me_body["name"] == registered_user["name"]
    print(me_body)

# -------------------------
# PATCH /api/profile -> change name, phone, address
# -------------------------
def test_patch_api_profile(api_context, registered_user, login_get_token):
    new_name = "Tam QA"
    new_phone = "0901118886"
    new_address = "Tan Phu - HCM"
    email = registered_user["email"]

    user_api = UserAPI(api_context)
    patch_resp = user_api.patch_profile(login_get_token, email, new_name, new_phone, new_address)
    assert patch_resp.status == 200, f"PATCH /api/profile failed: {patch_resp.status} - {patch_resp.text()}"
    patch_body = patch_resp.json()
    assert patch_body["msg"] == "Updated profile successfully."

    # Verify info by api/me
    me_resp = user_api.me(login_get_token)
    assert me_resp.status == 200, f"GET /api/me failed: {me_resp.status} - {me_resp.text()}"
    me_body = me_resp.json()
    assert me_body["name"] == new_name
    assert me_body["phone"] == new_phone
    assert me_body["address"] == new_address
    print(f"Update info {email} với new name: {new_name}, new phone: {new_phone}, new address: {new_address} succesfully!")
# -------------------------
# PATCH /api/profile -> change password
# -------------------------
def test_change_password_invalid_api(api_context, registered_user, login_get_token):
    user_api = UserAPI(api_context)
    # data change
    password_current = "ABC@1234"
    password_new = "NewPass@123"
    invalid_change_resp = user_api.patch_password(login_get_token, registered_user["email"], password_new, password_current)
    assert invalid_change_resp.status in [400, 401], \
        f"Expected invalid change password to fail, but got {invalid_change_resp.status} - {invalid_change_resp.text()}"
    
    print("Test case: Passed")

def test_change_password_valid_api(api_context, registered_user, login_get_token):
    user_api = UserAPI(api_context)
    # data change
    password_current = registered_user["password"]
    print(f"Password current: {password_current}")
    password_new = "NewPass@1234"
    print(f"Password current: {password_new}")
    valid_change_resp = user_api.patch_password(login_get_token, registered_user["email"], password_new, password_current)

    assert valid_change_resp.status == 200, \
        f"Valid change password failed: {valid_change_resp.status} - {valid_change_resp.text()}"
    valid_change_body = valid_change_resp.json()
    print(valid_change_body)
    assert "msg" in valid_change_body

    relogin = AuthAPI(api_context)
    relogin_resp = relogin.login(registered_user["email"], password_new)

    assert relogin_resp.status == 200, f"Re-login failed: {relogin_resp.status} - {relogin_resp.text()}"
    assert "accessToken" in relogin_resp.json()