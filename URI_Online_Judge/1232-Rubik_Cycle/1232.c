/*
Implementation of the Rubik Cycle challenge on URI Online Judge:
https://www.urionlinejudge.com.br/judge/en/problems/view/1232

Written in C99.

Author: Dorian Bolivar - Jan 2021.
*/

#include <stdio.h>
#include <string.h>

#define CUBE_SZ 3
#define TRUE 1
#define FALSE 0

short F[CUBE_SZ][CUBE_SZ] = { { 0, 0, 0 }, { 0, 0, 0 }, { 0, 0, 0 } };
short U[CUBE_SZ][CUBE_SZ] = { { 1, 1, 1 }, { 1, 1, 1 }, { 1, 1, 1 } };
short D[CUBE_SZ][CUBE_SZ] = { { 2, 2, 2 }, { 2, 2, 2 }, { 2, 2, 2 } };
short L[CUBE_SZ][CUBE_SZ] = { { 3, 3, 3 }, { 3, 3, 3 }, { 3, 3, 3 } };
short R[CUBE_SZ][CUBE_SZ] = { { 4, 4, 4 }, { 4, 4, 4 }, { 4, 4, 4 } };
short B[CUBE_SZ][CUBE_SZ] = { { 5, 5, 5 }, { 5, 5, 5 }, { 5, 5, 5 } };

void show(void)
{
	printf("F = [");
	for (short i = 0; i < CUBE_SZ; i++) {
		printf(" [");
		for (short j = 0; j < CUBE_SZ; j++)
			printf(" %d", F[i][j]);
		printf(" ]");
	}
	printf(" ]\n");

	printf("U = [");
	for (short i = 0; i < CUBE_SZ; i++) {
		printf(" [");
		for (short j = 0; j < CUBE_SZ; j++)
			printf(" %d", U[i][j]);
		printf(" ]");
	}
	printf(" ]\n");

	printf("D = [");
	for (short i = 0; i < CUBE_SZ; i++) {
		printf(" [");
		for (short j = 0; j < CUBE_SZ; j++)
			printf(" %d", D[i][j]);
		printf(" ]");
	}
	printf(" ]\n");

	printf("L = [");
	for (short i = 0; i < CUBE_SZ; i++) {
		printf(" [");
		for (short j = 0; j < CUBE_SZ; j++)
			printf(" %d", L[i][j]);
		printf(" ]");
	}
	printf(" ]\n");

	printf("R = [");
	for (short i = 0; i < CUBE_SZ; i++) {
		printf(" [");
		for (short j = 0; j < CUBE_SZ; j++)
			printf(" %d", R[i][j]);
		printf(" ]");
	}
	printf(" ]\n");

	printf("B = [");
	for (short i = 0; i < CUBE_SZ; i++) {
		printf(" [");
		for (short j = 0; j < CUBE_SZ; j++)
			printf(" %d", B[i][j]);
		printf(" ]");
	}
	printf(" ]\n");
}

short validate(void)
{
	for (short i = 0; i < CUBE_SZ; i++) {
		for (short j = 0; j < CUBE_SZ; j++) {
			if (F[i][j] != F[1][1] || U[i][j] != U[1][1] || D[i][j] != D[1][1] || L[i][j] != L[1][1] || R[i][j] != R[1][1] || B[i][j] != B[1][1]) {
				return FALSE;
			}
		}
	}

	return TRUE;
}

void face_rotate(short face[][CUBE_SZ], short face_t[][CUBE_SZ], char dir)
{
	short i, j;

	if (dir == 'c') {
		// Face rotate clockwise.
		for (j = 0; j <= 2; j += 2) {
			for (i = 0; i < CUBE_SZ; i++) {
				face[i][CUBE_SZ - 1 - j] = face_t[j][i];
				face[j][i] = face_t[CUBE_SZ - 1 - i][j];
			}
		}
	} else if (dir == 'a') {
		// Face rotate counterclockwise.
		for (j = 0; j <= 2; j += 2) {
			for (i = 0; i < CUBE_SZ; i++) {
				face[j][i] = face_t[i][CUBE_SZ - 1 - j];
				face[i][j] = face_t[j][CUBE_SZ - 1 - i];
			}
		}
	}
}

void rotate(char move)
{
	short i, j;

	// Temporary copies of the current face states.
	short Ft[CUBE_SZ][CUBE_SZ];
	short Ut[CUBE_SZ][CUBE_SZ];
	short Dt[CUBE_SZ][CUBE_SZ];
	short Lt[CUBE_SZ][CUBE_SZ];
	short Rt[CUBE_SZ][CUBE_SZ];
	short Bt[CUBE_SZ][CUBE_SZ];

	memcpy(Ft, F, sizeof(F));
	memcpy(Ut, U, sizeof(U));
	memcpy(Dt, D, sizeof(D));
	memcpy(Lt, L, sizeof(L));
	memcpy(Rt, R, sizeof(R));
	memcpy(Bt, B, sizeof(B));

	if (move == 'F') {
		face_rotate(F, Ft, 'c');

		for (i = 0; i < CUBE_SZ; i++) {
			U[2][i] = Lt[CUBE_SZ - 1 - i][2];
			L[i][2] = Dt[0][i];
			D[0][i] = Rt[CUBE_SZ - 1 - i][0];
			R[i][0] = Ut[2][i];
		}
	} else if (move == 'f') {
		face_rotate(F, Ft, 'a');

		for (i = 0; i < CUBE_SZ; i++) {
			U[2][i] = Rt[i][0];
			R[i][0] = Dt[0][CUBE_SZ - 1 - i];
			D[0][i] = Lt[i][2];
			L[i][2] = Ut[2][CUBE_SZ - 1 - i];
		}
	} else if (move == 'B') {
		face_rotate(B, Bt, 'c');

		for (i = 0; i < CUBE_SZ; i++) {
			U[0][i] = Rt[i][2];
			R[i][2] = Dt[2][CUBE_SZ - 1 - i];
			D[2][i] = Lt[i][0];
			L[i][0] = Ut[0][CUBE_SZ - 1 - i];
		}
	} else if (move == 'b') {
		face_rotate(B, Bt, 'a');

		for (i = 0; i < CUBE_SZ; i++) {
			U[0][i] = Lt[CUBE_SZ - 1 - i][0];
			L[i][0] = Dt[2][i];
			D[2][i] = Rt[CUBE_SZ - 1 - i][2];
			R[i][2] = Ut[0][i];
		}
	} else if (move == 'U') {
		face_rotate(U, Ut, 'c');

		for (i = 0; i < CUBE_SZ; i++) {
			B[2][i] = Lt[0][CUBE_SZ - 1 - i];
			L[0][i] = Ft[0][i];
			F[0][i] = Rt[0][i];
			R[0][i] = Bt[2][CUBE_SZ - 1 - i];
		}
	} else if (move == 'u') {
		face_rotate(U, Ut, 'a');

		for (i = 0; i < CUBE_SZ; i++) {
			B[2][i] = Rt[0][CUBE_SZ - 1 - i];
			R[0][i] = Ft[0][i];
			F[0][i] = Lt[0][i];
			L[0][i] = Bt[2][CUBE_SZ - 1 - i];
		}
	} else if (move == 'D') {
		face_rotate(D, Dt, 'c');

		for (i = 0; i < CUBE_SZ; i++) {
			F[2][i] = Lt[2][i];
			L[2][i] = Bt[0][CUBE_SZ - 1 - i];
			B[0][i] = Rt[2][CUBE_SZ - 1 - i];
			R[2][i] = Ft[2][i];
		}
	} else if (move == 'd') {
		face_rotate(D, Dt, 'a');

		for (i = 0; i < CUBE_SZ; i++) {
			F[2][i] = Rt[2][i];
			R[2][i] = Bt[0][CUBE_SZ - 1 - i];
			B[0][i] = Lt[2][CUBE_SZ - 1 - i];
			L[2][i] = Ft[2][i];
		}
	} else if (move == 'L') {
		face_rotate(L, Lt, 'c');

		for (i = 0; i < CUBE_SZ; i++) {
			U[i][0] = Bt[i][0];
			B[i][0] = Dt[i][0];
			D[i][0] = Ft[i][0];
			F[i][0] = Ut[i][0];
		}
	} else if (move == 'l') {
		face_rotate(L, Lt, 'a');

		for (i = 0; i < CUBE_SZ; i++) {
			U[i][0] = Ft[i][0];
			F[i][0] = Dt[i][0];
			D[i][0] = Bt[i][0];
			B[i][0] = Ut[i][0];
		}
	} else if (move == 'R') {
		face_rotate(R, Rt, 'c');

		for (i = 0; i < CUBE_SZ; i++) {
			U[i][2] = Ft[i][2];
			F[i][2] = Dt[i][2];
			D[i][2] = Bt[i][2];
			B[i][2] = Ut[i][2];
		}
	} else if (move == 'r') {
		face_rotate(R, Rt, 'a');

		for (i = 0; i < CUBE_SZ; i++) {
			U[i][2] = Bt[i][2];
			B[i][2] = Dt[i][2];
			D[i][2] = Ft[i][2];
			F[i][2] = Ut[i][2];
		}
	}
}

int main(void)
{
	char moves[82];
	short c, rounds;

	while (fgets(moves, 82, stdin) != NULL) {
		rounds = 1;

		while (TRUE) {
			c = 0;

			while (moves[c] != '\n' && moves[c] != '\0') {
				rotate(moves[c]);
				c++;
			}

			if (validate()) {
				break;
			} else {
				rounds++;
			}
		}

		printf("%d\n", rounds);
	}

	return 0;
}
