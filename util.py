import math

def get_angle(a, b, c):
    ax, ay = a
    bx, by = b
    cx, cy = c
    ab = (ax - bx, ay - by)
    cb = (cx - bx, cy - by)
    dot = ab[0]*cb[0] + ab[1]*cb[1]
    mag_ab = math.hypot(*ab)
    mag_cb = math.hypot(*cb)
    if mag_ab * mag_cb == 0:
        return 0
    cos_angle = dot / (mag_ab * mag_cb)
    angle = math.degrees(math.acos(cos_angle))
    return angle

def get_distance(points):
    (x1, y1), (x2, y2) = points
    return math.hypot(x2 - x1, y2 - y1)
