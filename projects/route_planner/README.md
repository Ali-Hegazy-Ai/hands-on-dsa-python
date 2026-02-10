# Route Planner

Find shortest paths between cities using custom graph and Dijkstra implementation.

## Goal

- Build a weighted graph from a CSV of city pairs and distances.
- Find shortest path between two cities using `dijkstra`.
- Print the path and total distance.

## Acceptance Criteria

- [ ] Matches known shortest paths for the test dataset.
- [ ] Handles disconnected nodes gracefully (raises `NoPathError`).
- [ ] Unit tests pass for graph construction, pathfinding, and edge cases.
- [ ] Writeup (<200 words) comparing Dijkstra vs Bellman-Ford on your dataset.

## Usage

```bash
python -m projects.route_planner.main cities.csv --from "CityA" --to "CityB"
```
