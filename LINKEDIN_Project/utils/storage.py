def inject_access_token(context, token: str):
    context.add_init_script(
        """
        (token) => {
            localStorage.setItem("accessToken", token);
        }
        """,
        token
    )
