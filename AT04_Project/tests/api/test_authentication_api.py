import pytest, requests
from page_api.user_api import UserAPI
from page_api.authentication_api import AuthAPI
import allure
# -------------------------
# Login API → lấy token
# -------------------------
@allure.description("Verify get user's token")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_by_api_get_token(login_get_token):
    with allure.step("Get user's token"):
        user_token = login_get_token
        print(f"User's Token : {user_token}")

# -------------------------
# GET /api/me
# -------------------------
@allure.description("Verify get user's token")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_api_me(api_context, registered_user, login_get_token):
    with allure.step("Get user's token"):
        token = login_get_token
        headers = {"Authorization": f"Bearer {token}"}
    with allure.step("Get API response's user"):
        user_api = UserAPI(api_context)
        me_resp = user_api.me(token)
    with allure.step("Verify API's status"):
        assert me_resp.status == 200, f"GET /api/me failed: {me_resp.status} - {me_resp.text()}"
    with allure.step("Verify that the displayed email and name correspond to the logged-in account."):
        me_body = me_resp.json()
        assert me_body["email"] == registered_user["email"]
        assert me_body["name"] == registered_user["name"]
        print(me_body)

# -------------------------
# PATCH /api/profile -> change name, phone, address
# -------------------------
@allure.description("Verify PATCH /api/profile -> change name, phone, address ")
@allure.severity(allure.severity_level.CRITICAL)
def test_patch_api_profile(api_context, registered_user, login_get_token):
    with allure.step("Generate data that needs to be updated."):
        new_name = "Tam QA"
        new_phone = "0901118886"
        new_address = "Tan Phu - HCM"
        email = registered_user["email"]
    with allure.step("Update API Patch profile with change name, phone, address"):
        user_api = UserAPI(api_context)
        patch_resp = user_api.patch_profile(login_get_token, email, new_name, new_phone, new_address)
    with allure.step("Verify API's status"):    
        assert patch_resp.status == 200, f"PATCH /api/profile failed: {patch_resp.status} - {patch_resp.text()}"
    with allure.step("Verify Patch's body with message: Updated profile successfully."):  
        patch_body = patch_resp.json()
        assert patch_body["msg"] == "Updated profile successfully."
    with allure.step("Verify info by api/me"): 
        me_resp = user_api.me(login_get_token)
        assert me_resp.status == 200, f"GET /api/me failed: {me_resp.status} - {me_resp.text()}"
    with allure.step("Verify that the updated information is correctly reflected according to the generated test data"):
        me_body = me_resp.json()
        assert me_body["name"] == new_name
        assert me_body["phone"] == new_phone
        assert me_body["address"] == new_address
        print(f"Update info {email} với new name: {new_name}, new phone: {new_phone}, new address: {new_address} succesfully!")
# -------------------------
# PATCH /api/profile -> change password
# -------------------------
@allure.description("Verify the Change Password API with an invalid password.")
@allure.severity(allure.severity_level.CRITICAL)
def test_change_password_invalid_api(api_context, registered_user, login_get_token):
    with allure.step("Generate data password"):
        user_api = UserAPI(api_context)
    # data change
        password_current = "ABC@1234"
        password_new = "NewPass@123"
    with allure.step("Run API change password with invalid password"):    
        invalid_change_resp = user_api.patch_password(login_get_token, registered_user["email"], password_new, password_current)
    with allure.step("Verify API's status response status code is 400 or 401"):     
        assert invalid_change_resp.status in [400, 401], \
            f"Expected invalid change password to fail, but got {invalid_change_resp.status} - {invalid_change_resp.text()}"
        print("Test case: Passed")

@allure.description("Verify the Change Password API with an valid password.")
@allure.severity(allure.severity_level.CRITICAL)
def test_change_password_valid_api(api_context, registered_user, login_get_token):
    with allure.step("Generate data password"):
        user_api = UserAPI(api_context)
    # data change
        password_current = registered_user["password"]
        # print(f"Password current: {password_current}")
        password_new = "NewPass@1234"
        # print(f"Password current: {password_new}")
    with allure.step("Run API change password with valid password"):     
        valid_change_resp = user_api.patch_password(login_get_token, registered_user["email"], password_new, password_current)
    with allure.step("Verify API's status response status code"):
        assert valid_change_resp.status == 200, \
            f"Valid change password failed: {valid_change_resp.status} - {valid_change_resp.text()}"
    with allure.step("Verify body after run API successfully"):    
        valid_change_body = valid_change_resp.json()
        # print(valid_change_body)
        assert "msg" in valid_change_body
    with allure.step("Run API with new password"):  
        relogin = AuthAPI(api_context)
        relogin_resp = relogin.login(registered_user["email"], password_new)
    with allure.step("Verify login successfully with new password"):  
        assert relogin_resp.status == 200, f"Re-login failed: {relogin_resp.status} - {relogin_resp.text()}"
        assert "accessToken" in relogin_resp.json()