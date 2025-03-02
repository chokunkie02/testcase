def determine_winner(cat_a, cat_b, mouse):
    distance_a = abs(cat_a - mouse)
    distance_b = abs(cat_b - mouse)
    
    if distance_a < distance_b:
        return "Cat A"
    elif distance_b < distance_a:
        return "Cat B"
    else:
        return "Mouse C"