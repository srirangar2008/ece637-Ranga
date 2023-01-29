#ifndef DEFS_H
#define DEFS_H

struct pixel 
{
    int m; // row index
    int n; // col index
};

typedef struct pixel Pixel;

//Fucntions
void ConnectedNeighbours(
    Pixel s, 
    double T, 
    unsigned char** img, 
    int width, 
    int height, 
    int *M, 
    Pixel c[4]
);

void ConnectedSet(
    Pixel s, 
    double T, 
    unsigned char** img, 
    int width, 
    int height, 
    int ClassLabel,
    unsigned int **seg, 
    int *NumConPixels 
);

#endif