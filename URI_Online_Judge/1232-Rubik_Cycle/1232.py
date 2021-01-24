"""
Implementation of the Rubik Cycle challenge on URI Online Judge:
https://www.urionlinejudge.com.br/judge/en/problems/view/1232

Written in Python 3.

Author: Dorian Bolivar - Jan 2021.
"""

#from copy import deepcopy
from sys import stdin, stdout

F = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
U = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
D = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
L = [[3, 3, 3], [3, 3, 3], [3, 3, 3]]
R = [[4, 4, 4], [4, 4, 4], [4, 4, 4]]
B = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
CUBE_SZ = 3


def show(faces: str = "F,U,D,L,R,B"):
	for face in faces.split(","):
		print(f"{face.strip()}:\n{eval(face)}")


def validate():
	for i in range(CUBE_SZ):
		for j in range(CUBE_SZ):
			if (F[i][j] != F[1][1] or U[i][j] != U[1][1] or D[i][j] != D[1][1] or L[i][j] != L[1][1] or R[i][j] != R[1][1] or B[i][j] != B[1][1]):
				return False

	return True


def face_rotate(face: list, face_t: list, dir: str):
	if (dir == "c"):
		for j in range(0, 3, 2):
			for i in range(CUBE_SZ):
				face[i][CUBE_SZ - 1 - j] = face_t[j][i]
				face[j][i] = face_t[CUBE_SZ - 1 - i][j]
	elif (dir == "a"):
		for j in range(0, 3, 2):
			for i in range(CUBE_SZ):
				face[j][i] = face_t[i][CUBE_SZ - 1 - j]
				face[i][j] = face_t[j][CUBE_SZ - 1 - i]


def rotate(move: str):
	# deepcopy() is extremely slow!
	#Ft = deepcopy(F)
	#Ut = deepcopy(U)
	#Dt = deepcopy(D)
	#Lt = deepcopy(L)
	#Rt = deepcopy(R)
	#Bt = deepcopy(B)

	Ft = [[F[x][y] for y in range(len(F[0]))] for x in range(len(F))]
	Ut = [[U[x][y] for y in range(len(U[0]))] for x in range(len(U))]
	Dt = [[D[x][y] for y in range(len(D[0]))] for x in range(len(D))]
	Lt = [[L[x][y] for y in range(len(L[0]))] for x in range(len(L))]
	Rt = [[R[x][y] for y in range(len(R[0]))] for x in range(len(R))]
	Bt = [[B[x][y] for y in range(len(B[0]))] for x in range(len(B))]

	if (move == "F"):
		face_rotate(F, Ft, "c")

		for i in range(CUBE_SZ):
			U[2][i] = Lt[CUBE_SZ - 1 - i][2]
			L[i][2] = Dt[0][i]
			D[0][i] = Rt[CUBE_SZ - 1 - i][0]
			R[i][0] = Ut[2][i]
	elif (move == "f"):
		face_rotate(F, Ft, "a")

		for i in range(CUBE_SZ):
			U[2][i] = Rt[i][0]
			R[i][0] = Dt[0][CUBE_SZ - 1 - i]
			D[0][i] = Lt[i][2]
			L[i][2] = Ut[2][CUBE_SZ - 1 - i]
	elif (move == "B"):
		face_rotate(B, Bt, "c")

		for i in range(CUBE_SZ):
			U[0][i] = Rt[i][2]
			R[i][2] = Dt[2][CUBE_SZ - 1 - i]
			D[2][i] = Lt[i][0]
			L[i][0] = Ut[0][CUBE_SZ - 1 - i]
	elif (move == "b"):
		face_rotate(B, Bt, "a")

		for i in range(CUBE_SZ):
			U[0][i] = Lt[CUBE_SZ - 1 - i][0]
			L[i][0] = Dt[2][i]
			D[2][i] = Rt[CUBE_SZ - 1 - i][2]
			R[i][2] = Ut[0][i]
	elif (move == "U"):
		face_rotate(U, Ut, "c")

		for i in range(CUBE_SZ):
			B[2][i] = Lt[0][CUBE_SZ - 1 - i]
			L[0][i] = Ft[0][i]
			F[0][i] = Rt[0][i]
			R[0][i] = Bt[2][CUBE_SZ - 1 - i]
	elif (move == "u"):
		face_rotate(U, Ut, "a")

		for i in range(CUBE_SZ):
			B[2][i] = Rt[0][CUBE_SZ - 1 - i]
			R[0][i] = Ft[0][i]
			F[0][i] = Lt[0][i]
			L[0][i] = Bt[2][CUBE_SZ - 1 - i]
	elif (move == "D"):
		face_rotate(D, Dt, "c")

		for i in range(CUBE_SZ):
			F[2][i] = Lt[2][i]
			L[2][i] = Bt[0][CUBE_SZ - 1 - i]
			B[0][i] = Rt[2][CUBE_SZ - 1 - i]
			R[2][i] = Ft[2][i]
	elif (move == "d"):
		face_rotate(D, Dt, "a")

		for i in range(CUBE_SZ):
			F[2][i] = Rt[2][i]
			R[2][i] = Bt[0][CUBE_SZ - 1 - i]
			B[0][i] = Lt[2][CUBE_SZ - 1 - i]
			L[2][i] = Ft[2][i]
	elif (move == "L"):
		face_rotate(L, Lt, "c")

		for i in range(CUBE_SZ):
			U[i][0] = Bt[i][0]
			B[i][0] = Dt[i][0]
			D[i][0] = Ft[i][0]
			F[i][0] = Ut[i][0]
	elif (move == "l"):
		face_rotate(L, Lt, "a")

		for i in range(CUBE_SZ):
			U[i][0] = Ft[i][0]
			F[i][0] = Dt[i][0]
			D[i][0] = Bt[i][0]
			B[i][0] = Ut[i][0]
	elif (move == "R"):
		face_rotate(R, Rt, "c")

		for i in range(CUBE_SZ):
			U[i][2] = Ft[i][2]
			F[i][2] = Dt[i][2]
			D[i][2] = Bt[i][2]
			B[i][2] = Ut[i][2]
	elif (move == "r"):
		face_rotate(R, Rt, "a")

		for i in range(CUBE_SZ):
			U[i][2] = Bt[i][2]
			B[i][2] = Dt[i][2]
			D[i][2] = Ft[i][2]
			F[i][2] = Ut[i][2]


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
