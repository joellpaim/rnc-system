from functools import wraps
from flask_login import current_user


def admin_only(func):	
	""" Decorator for giving access to authorized users only """
	@wraps(func)
	def wrapper(*args, **kwargs):
		for role in current_user.roles:
			if current_user.is_authenticated and role.name == "Admin":
				return func(*args, **kwargs)
			else:
				return "Você não está autorizado a acessar esta URL."
	wrapper.__name__ = func.__name__
	return wrapper