# Rightpath-Safety-Route-Map-for-SJSU-
Risk-aware campus navigation using data science and GIS
## Overview
RightPath is a data-driven campus navigation system designed to prioritize student safety over shortest-distance routing. Traditional navigation tools optimize for time and distance but do not account for safety conditions such as lighting, incident density, or security patrol coverage.

## Research Question
How can data science and GIS-based routing be used to generate safer on-campus walking routes that reduce exposure to risk compared with shortest-path navigation?

## Key Features
- Risk-aware routing using graph-based algorithms
- Composite edge weights combining distance and safety risk
- Integration of heterogeneous safety data sources
- Visual analytics including risk heatmaps and hotspot dashboards

## Technical Approach
- Campus walkways modeled as a weighted graph
- Edges weighted by distance and safety risk
- Composite cost minimized using Dijkstra or A*
- Tunable safety–distance parameter

## Technologies
Python, NetworkX, GeoPandas, Pandas, Matplotlib, Plotly

## Authors
Jatesh Joshi
