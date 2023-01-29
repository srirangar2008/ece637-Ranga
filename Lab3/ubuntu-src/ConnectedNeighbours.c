#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include "defs.h"

void ConnectedNeighbours(
    Pixel s, double T, unsigned char** img, 
    int width, int height, int *M, Pixel c[4] )
{
    int neighbours = 0;
    //Calculating the neighbors of s.
    int x = s.m; // row index of image
    int y = s.n; // col index of image
    if((x - 1 >= 0) && abs(img[x][y] - img[x-1][y]) <= T)
    {
        c[neighbours].m = x - 1;
        c[neighbours].n = y;
        neighbours++;
    }
    if((x + 1 < height) && abs(img[x][y] - img[x+1][y]) <= T)
    {
        c[neighbours].m = x + 1;
        c[neighbours].n = y;
        neighbours++; 
    }
    if((y - 1 >= 0) && abs(img[x][y] - img[x][y-1]) <= T)
    {
        c[neighbours].m = x;
        c[neighbours].n = y - 1;
        neighbours++;
    }
    if((y + 1 < width) && abs(img[x][y] - img[x][y+1]) <= T)
    {
        c[neighbours].m = x;
        c[neighbours].n = y + 1;
        neighbours++;
    }
    *M = neighbours;
    /*printf("Connected components of %d, %d are with neighbors = %d\n", s.m, s.n, neighbours);
    for(int i = 0; i < neighbours; i++)
    {
        printf("m = %d, n = %d\n", c[i].m, c[i].n);
    }*/
    return;
}

void ConnectedSet(
    Pixel s, double T, unsigned char** img, int width, 
    int height, int ClassLabel,unsigned int **seg, int *NumConPixels )
{
    //printf("Entered connected set\n");
    int count = 0;
    int connectedPixels = 0;
    Pixel c[4];
    ConnectedNeighbours(s, T, img, width, height, &connectedPixels, c);
    if(connectedPixels == 0)
    {
        //printf("Returning now\n");
        return;
    }
    
    for(int i = 0; i < connectedPixels; i++)
    {
        if(seg[c[i].m][c[i].n] != ClassLabel)
        {
            printf("Pixel Coordinate - %d, %d set to 1.\n", c[i].m, c[i].n);
            seg[c[i].m][c[i].n] = ClassLabel;
            count++;
            ConnectedSet(c[i], T, img, width, height, ClassLabel, seg, NumConPixels);
        }
    }
    //printf("Recursion ended\n");
    *NumConPixels += count;
    return;
}
