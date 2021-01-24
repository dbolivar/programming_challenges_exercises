"""
Implementation of the Rubik Cycle challenge on URI Online Judge:
https://www.urionlinejudge.com.br/judge/en/problems/view/1232

Written in Python 3 with NumPy.

Author: Dorian Bolivar - Jan 2021.
"""

import numpy as np
from sys import stdin, stdout

f = np.full((3, 3), 0, dtype=int)
u = np.full((3, 3), 1, dtype=int)
d = np.full((3, 3), 2, dtype=int)
l = np.full((3, 3), 3, dtype=int)
r = np.full((3, 3), 4, dtype=int)
b = np.full((3, 3), 5, dtype=int)


def show(faces: str = "f,u,d,l,r,b"):
	for face in faces.split(","):
		print(f"{face.strip()}:\n{eval(face)}")


def validate():
	if (np.any(f != 0) or np.any(u != 1) or np.any(d != 2) or np.any(l != 3) or np.any(r != 4) or np.any(b != 5)):
		return False

	return True


def rotate(move: str):
	global f, u, d, l, r, b

	# Uppercase: clockwise. Lowercase: counterclockwise.
	if (move in "Ff"):
		# Face rotate.
		f = np.rot90(f, -1 if move.isupper() else 1)

		# Edges rotation.
		if (move.isupper()):
			u[2, :], l[:, 2], d[0, :], r[:, 0] = np.flip(l[:, 2]).copy(), d[0, :].copy(), np.flip(r[:, 0]).copy(), u[2, :].copy()
		else:
			u[2, :], r[:, 0], d[0, :], l[:, 2] = r[:, 0].copy(), np.flip(d[0, :]).copy(), l[:, 2].copy(), np.flip(u[2, :]).copy()
	elif (move in "Uu"):
		# Face rotate.
		u = np.rot90(u, -1 if move.isupper() else 1)

		# Edges rotation.
		if (move.isupper()):
			b[2, :], l[0, :], f[0, :], r[0, :] = np.flip(l[0, :]).copy(), f[0, :].copy(), r[0, :].copy(), np.flip(b[2, :]).copy()
		else:
			b[2, :], r[0, :], f[0, :], l[0, :] = np.flip(r[0, :]).copy(), f[0, :].copy(), l[0, :].copy(), np.flip(b[2, :]).copy()
	elif (move in "Dd"):
		# Face rotate.
		d = np.rot90(d, -1 if move.isupper() else 1)

		# Edges rotation.
		if (move.isupper()):
			f[2, :], l[2, :], b[0, :], r[2, :] = l[2, :].copy(), np.flip(b[0, :]).copy(), np.flip(r[2, :]).copy(), f[2, :].copy()
		else:
			f[2, :], r[2, :], b[0, :], l[2, :] = r[2, :].copy(), np.flip(b[0, :]).copy(), np.flip(l[2, :]).copy(), f[2, :].copy()
	elif (move in "Ll"):
		# Face rotate.
		l = np.rot90(l, -1 if move.isupper() else 1)

		# Edges rotation.
		if (move.isupper()):
			u[:, 0], b[:, 0], d[:, 0], f[:, 0] = b[:, 0].copy(), d[:, 0].copy(), f[:, 0].copy(), u[:, 0].copy()
		else:
			u[:, 0], f[:, 0], d[:, 0], b[:, 0] = f[:, 0].copy(), d[:, 0].copy(), b[:, 0].copy(), u[:, 0].copy()
	elif (move in "Rr"):
		# Face rotate.
		r = np.rot90(r, -1 if move.isupper() else 1)

		# Edges rotation.
		if (move.isupper()):
			u[:, 2], f[:, 2], d[:, 2], b[:, 2] = f[:, 2].copy(), d[:, 2].copy(), b[:, 2].copy(), u[:, 2].copy()
		else:
			u[:, 2], b[:, 2], d[:, 2], f[:, 2] = b[:, 2].copy(), d[:, 2].copy(), f[:, 2].copy(), u[:, 2].copy()
	elif (move in "Bb"):
		# Face rotate.
		b = np.rot90(b, -1 if move.isupper() else 1)

		# Edges rotation.
		if (move.isupper()):
			u[0, :], r[:, 2], d[2, :], l[:, 0] = r[:, 2].copy(), np.flip(d[2, :]).copy(), l[:, 0].copy(), np.flip(u[0, :]).copy()
		else:
			u[0, :], l[:, 0], d[2, :], r[:, 2] = np.flip(l[:, 0]).copy(), d[2, :].copy(), np.flip(r[:, 2]).copy(), u[0, :].copy()


for moves in stdin.readlines():
	moves = moves.strip()

	#if (any(move not in "FfUuDdLlRrBb" for move in moves)):
	#	print("Invalid move detected:", moves)
	#	exit(1)

	rounds = 1

	while True:
		for move in moves:
			rotate(move)

		if (validate()):
			break
		else:
			rounds += 1

	stdout.write(str(rounds) + "\n")
