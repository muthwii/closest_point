from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .serializers import closest_point_serializer
from . models import closest_point
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_200_OK,
    HTTP_200_OK
)

#function to get the closest points
def close_Point(points, K):
    #use merge sort to check the closest points
    points.sort(key = lambda K: K[0]**2 + K[1]**2)
 
    return points[:K]

@api_view(['POST'])
def c_point(request):
    #get serializer data    
    serializer = closest_point_serializer(data=request.data)
    if serializer.is_valid():
        point=serializer.data['points']
        #convert to an array
        points = eval('[' + point + ']')
        K = 2 
        #call the function to calculate the closest points       
        cpoints = close_Point(points, K)
        #save to the database
        Sv=closest_point(
                        points=point,
                        closest_points_pair=cpoints                                         

                    )
        Sv.save() 
        #return response        
        return Response({'Success': 'True', 'Code': 200,'closest_points': cpoints},
                                status=HTTP_200_OK)
    return Response(data=serializer.errors,status=HTTP_400_BAD_REQUEST) 

    
         
            
    

