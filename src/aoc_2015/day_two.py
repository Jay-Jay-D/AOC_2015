from math import prod

def get_surface_area(l,w,h):
    return 2*l*w + 2*w*h + 2*h*l

def get_area_smallest_side_area(*dimensions):
    return prod(dimensions[:2:1])

if __name__ == "__main__":
    print(get_area_smallest_side_area(2,3,4))
    print(get_area_smallest_side_area(1,1,10))