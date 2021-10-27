import gpxpy
import gpxpy.gpx
import math

def distanceBetweenCoordinates(lat1, lon1, lat2, lon2):
    earthRadiusKm = 6371

    dLat = math.radians(lat2-lat1)
    dLon = math.radians(lon2-lon1)

    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)

    a = math.sin(dLat/2) * math.sin(dLat/2) + math.sin(dLon/2) * math.sin(dLon/2) * math.cos(lat1) * math.cos(lat2) 
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a)) 
    return earthRadiusKm * c

def get_distance(path):
    total_dis = 0
    tmp_point = None

    gpx_file = open(path, "r")
    tour = gpxpy.parse(gpx_file)
    for track in tour.tracks:
        for segment in track.segments:
            for point in segment.points:
                if tmp_point is None: tmp_point = point
                total_dis += distanceBetweenCoordinates(point.latitude, point.longitude, tmp_point.latitude, tmp_point.longitude)
                tmp_point = point

    return total_dis

def get_elevation(path, positive=True):
    total_ele = 0
    tmp_point = None

    gpx_file = open(path, "r")
    tour = gpxpy.parse(gpx_file)
    if positive:
        for track in tour.tracks:
            for segment in track.segments:
                for point in segment.points:
                    if tmp_point is None: tmp_point = point
                    if point.elevation > tmp_point.elevation: total_ele += point.elevation - tmp_point.elevation
                    tmp_point = point
    else:
        for track in tour.tracks:
            for segment in track.segments:
                for point in segment.points:
                    if tmp_point is None: tmp_point = point
                    if point.elevation < tmp_point.elevation: total_ele += point.elevation - tmp_point.elevation
                    tmp_point = point

    return total_ele