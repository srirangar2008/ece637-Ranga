# For Linux or any machines with gcc compiler
CC = gcc 
CFLAGS = -std=c99 -Wall -pedantic
BIN = ../bin

all: ConnectedSet

clean:
	/bin/rm *.o

OBJ = tiff.o allocate.o randlib.o qGGMRF.o solve.o ConnectedNeighbours.o

ImageReadWriteExample: ImageReadWriteExample.o $(OBJ) 
	$(CC) $(CFLAGS) -o ImageReadWriteExample ImageReadWriteExample.o $(OBJ) -lm
	mv ImageReadWriteExample $(BIN)

SurrogateFunctionExample: SurrogateFunctionExample.o $(OBJ) 
	$(CC) $(CFLAGS) -o SurrogateFunctionExample SurrogateFunctionExample.o $(OBJ) -lm
	mv SurrogateFunctionExample $(BIN)

SolveExample: SolveExample.o $(OBJ) 
	$(CC) $(CFLAGS) -o SolveExample SolveExample.o $(OBJ) -lm
	mv SolveExample $(BIN)

ConnectedSet: main.o $(OBJ)
	$(CC) $(CFLAGS) -g -o ConnectedNeighbours main.c $(OBJ) -lm
	mv ConnectedNeighbours.exe ConnectedNeighbours

ConnectedSetDebug: main.o $(OBJ)
	$(CC) $(CFLAGS) -DDEBUG -g -o ConnectedNeighbours_debug main.c $(OBJ) -lm
	mv ConnectedNeighbours_debug.exe ConnectedNeighbours_debug


