def clear_block(block, state):

    return block not in state.values()


def move_to_table(block, state, actions):

    if not clear_block(block, state):

        above = next(
            b for b, support in state.items()
            if support == block
        )

        move_to_table(above, state, actions)

    old_support = state[block]

    if old_support != "table":

        state[block] = "table"

        actions.append(
            f"Move {block} from {old_support} to table"
        )


def goal_stack_plan(initial, goal):

    state = initial.copy()

    actions = []

    for block, target in goal.items():

        if block not in state:
            raise ValueError("Unknown block")

        if target != "table" and target not in state:
            raise ValueError("Unknown support block")

        if state[block] == target:
            continue

        move_to_table(block, state, actions)

        if target != "table":
            move_to_table(target, state, actions)

        state[block] = target

        actions.append(
            f"Move {block} onto {target}"
        )

    return state, actions


initial = {
    "A": "table",
    "B": "A",
    "C": "table"
}

goal = {
    "A": "table",
    "B": "table",
    "C": "B"
}

final_state, plan = goal_stack_plan(initial, goal)

print("Goal Stack Plan:")

for step in plan:
    print(step)

print("Final State:", final_state)