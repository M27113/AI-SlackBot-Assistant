from ai_handler import get_ai_response

def plan_tasks(goal):
    prompt = f"Create a day-by-day actionable plan for the goal:\n{goal}"
    return get_ai_response(prompt)
