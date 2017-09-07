from passwordhelper import PasswordHelper
from mockdbhelper.py import MockdbHelper

PH = PasswordHelper()
DB = MockdbHelper()

@app.route("/login", methods=["POST"])
def login():
	email = request.form.get("email")
	password = request.form.get("password")
	stored_user = DB.get_user(email)
	if stored_user and PH.validate_password(password,stored_user['salt'], stored_user['hashed']):
		user = User(email)
		login_user(user, remember=True)
		return redirect(url_for('account'))
	return home()

@app.route("/register", methods=["POST"])
def register():
	email = request.form.get("email")
	pw1 = request.form.get("password")
	pw2 = request.form.get("password2")
	if not pw1 == pw2:
		return redirect(url_for('home'))
	if DB.get_user(email):
		return redirect(url_for('home'))
	salt = PH.get_salt()
	hashed = PH.get_hash(pw1 + salt)
	DB.add_user(email, salt, hashed)
	return redirect(url_for('home'))
