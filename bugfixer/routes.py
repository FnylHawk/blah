from flask import Blueprint, request, jsonify
from collections import defaultdict, deque

# Create a Blueprint for bugfixer
bugfixer_bp = Blueprint('bugfixer', __name__)

# Helper function to calculate the minimum hours needed
def calculate_min_hours(time, prerequisites):
    n = len(time)
    time = [0] + time  # Convert 1-based index to 0-based for easier handling

    adj_list = defaultdict(list)
    in_degree = [0] * (n + 1)

    # Build the graph and calculate in-degree
    for a, b in prerequisites:
        adj_list[a].append(b)
        in_degree[b] += 1

    queue = deque()
    min_time = [0] * (n + 1)

    # Initially enqueue all projects with no prerequisites
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)
            min_time[i] = time[i]

    # Process in topological order
    while queue:
        current = queue.popleft()
        for neighbor in adj_list[current]:
            in_degree[neighbor] -= 1
            min_time[neighbor] = max(min_time[neighbor], min_time[current] + time[neighbor])
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return max(min_time)

# Define the route for the bugfixer
@bugfixer_bp.route('/bugfixer/p1', methods=['POST'])
def bugfixer():
    data = request.json
    results = []

    for entry in data:
        time = entry['time']
        prerequisites = entry['prerequisites']
        min_hours = calculate_min_hours(time, prerequisites)
        results.append(min_hours)

    return jsonify(results)
