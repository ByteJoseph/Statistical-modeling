//  write a program to find surface area and volume of a cylinder using functions
//  A=2πrh+2πr^2 
//  V= pi r^2 h

#include <stdio.h>
float area(float,float);
float volume(float,float);

int main(){
    float a,b,_area,_volume;
    printf("Enter the radius: ");
    scanf("%f",&a);
    printf("Enter the height: ");
    scanf("%f",&b);
    _area = area(a,b);
    _volume = volume(a,b);
    printf("Area = %f \nVolume = %f",_area,_volume);
    return 0;
}

float area(float r, float h){
    return (2*3.14*r*h)+(2*3.14*(r*r));
}

float volume(float r, float h){
    return (3.14*(r*r)*h);
}