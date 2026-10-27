import os
from functools import wraps

from flask import Flask, redirect, request, session, url_for
from itsdangerous import URLSafeTimedSerializer

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
app.config["SESSION_COOKIE_SECURE"] = True

serializer = URLSafeTimedSerializer(app.secret_key)


def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if not session.get("admin"):
            return "Login required", 401
        return view(*args, **kwargs)

    return wrapped


@app.route("/auth")
def auth():
    token = request.args.get("token")
    if not token:
        return "Missing token", 400

    try:
        user_id = serializer.loads(
            token,
            salt="admin-login",
            max_age=300,
        )
    except Exception:
        return "Invalid or expired token", 401

    # In production, the member record is checked in SQLite here.
    is_admin = lookup_admin_role(user_id)
    if not is_admin:
        return "Forbidden", 403

    session["admin"] = True
    return redirect(url_for("home"))


def lookup_admin_role(user_id):
    """Portfolio placeholder for the production DB role check."""
    raise NotImplementedError
