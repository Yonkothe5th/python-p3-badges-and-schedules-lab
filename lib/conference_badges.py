def badge_maker(name):
    return f'Hello, my name is {name}.'

def batch_badge_creator(names):
    badges = [badge_maker(name) for name in names]
    return badges


def assign_rooms(names):
    assignments = []
    for room in range(1, 9):
        assignments.append(f'Hello, {names[room - 1]}! You\'ll be assigned to room {room}!')
    return assignments
def printer(names):
    for badge in batch_badge_creator(names):
        print(badge)
    
    for assignment in assign_rooms(names):
        print(assignment)
