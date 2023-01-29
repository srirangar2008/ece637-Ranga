#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <math.h>
#include "tiff.h"
#include "allocate.h"
#include "randlib.h"
#include "typeutil.h"
#include "defs.h"

//clear the allocated variables as well. 

void help()
{
    printf(" arg1 : Input Image, \n \
             arg2 : m-co-ordinate of img, \n \
             arg3 : n-co-ordiate of img, \n \
             arg4 : threshold T, \n \
             arg5 : ClassLabel L, \n");
}

int main(int argc, char* argv[])
{
  FILE *fp;
  struct TIFF_img input_img, output_tiff; 

  if ( argc != 6 ) 
  {
    help();
    //error( argv[0] );
    exit(0);
  }
  //Testing the connected neighbour subroutine
    Pixel s;
    s.m = atoi(argv[2]);
    s.n = atoi(argv[3]);
    double T = atoi(argv[4]);
    int ClassLabel = atoi(argv[5]);

  /* open image file */
  if ( ( fp = fopen ( argv[1], "rb" ) ) == NULL ) {
    fprintf ( stderr, "cannot open file %s\n", argv[1] );
    exit ( 1 );
  }

  /* read image */
  if ( read_TIFF ( fp, &input_img ) ) {
    fprintf ( stderr, "error reading file %s\n", argv[1] );
    exit ( 1 );
  }

  /* close image file */
  fclose ( fp );

  /* check the type of image data */
  if ( input_img.TIFF_type != 'g' ) {
    fprintf ( stderr, "error:  image must be gray scale\n" );
    exit ( 1 );
  }


   unsigned int** seg = (unsigned int**)get_img(input_img.width, input_img.height, sizeof(unsigned int));
   for(int i = 0; i < input_img.height; i++)
   {
    for(int j = 0; j < input_img.width; j++)
    {
        seg[i][j] = 0;
    }
   }
   get_TIFF ( &output_tiff, input_img.height, input_img.width, 'g' );
   for(int i = 0; i < input_img.height; i++)
   {
    for(int j = 0; j < input_img.width; j++)
    {
        output_tiff.mono[i][j] = 0;
    }
   }
   
    int connectedPixels = 0;
    ConnectedSet(s, T, input_img.mono, input_img.width, input_img.height, ClassLabel, seg, &connectedPixels);
    printf("Connected Pixesls = %d\n", connectedPixels);
    for(int i = 0; i < input_img.height; i++)
    {
    for(int j = 0; j < input_img.width; j++)
    {
        if(seg[i][j] == 1)
        {
            output_tiff.mono[i][j] = 255;
        }
    }
    }

    if ( ( fp = fopen ( "output.tif", "wb" ) ) == NULL ) {
    fprintf ( stderr, "cannot open file output.tif\n");
    exit ( 1 );
    }

    /* write green image */
    if ( write_TIFF ( fp, &output_tiff ) ) {
    fprintf ( stderr, "error writing TIFF file %s\n", argv[2] );
    exit ( 1 );
    }
    
    fclose ( fp );
    #if 1
    ClassLabel = 1;
    get_TIFF ( &output_tiff, input_img.height, input_img.width, 'g' );
    for(int i = 0; i < input_img.height; i++)
    {
        for(int j = 0; j < input_img.width; j++)
        {
            output_tiff.mono[i][j] = 0;
        }
    }
    for(int i = 0; i < input_img.height; i++)
    {
        for(int j = 0; j < input_img.width; j++)
        {
            seg[i][j] = 0;
        }
    }

    for(int i = 0; i < input_img.height; i++)
    //for(int i = 145; i < 160; i++)
    {
        printf("i = %d\n", i);
        for(int j = 0; j < input_img.width; j++)
        //for(int j = 145; j < 160; j++)
        {
            connectedPixels = 0;
            if(seg[i][j] == 0)
            {
                s.m = i;
                s.n = j;
                ConnectedSet(s, T, input_img.mono, input_img.width, input_img.height, ClassLabel, seg, &connectedPixels);
                if(connectedPixels > 100)
                {
                    printf("Pixel : m = %d, n = %d, connected pixels = %d\n", s.m, s.n, connectedPixels);
                    ClassLabel++;
                }
                else
                {
                    printf("Pixel : m = %d, n = %d, connected pixels = %d\n", s.m, s.n, connectedPixels);
                    ConnectedSet(s, T, input_img.mono, input_img.width, input_img.height, 0, seg, &connectedPixels);
                }
            }
        }
    }

    for(int i = 0; i < input_img.height; i++)
    {
        for(int j = 0; j < input_img.width; j++)
        {
            if(seg[i][j] != 0)
            {
                output_tiff.mono[i][j] = seg[i][j];
            }
        }
    }

    if ( ( fp = fopen ( "output_segment.tif", "wb" ) ) == NULL ) {
    fprintf ( stderr, "cannot open file output.tif\n");
    exit ( 1 );
    }

    /* write green image */
    if ( write_TIFF ( fp, &output_tiff ) ) {
    fprintf ( stderr, "error writing TIFF file %s\n", argv[2] );
    exit ( 1 );
    }

    fclose ( fp );
    #endif
    free_TIFF(&input_img);
    free_TIFF(&output_tiff);
    free_img(seg);

  return 0;
}

