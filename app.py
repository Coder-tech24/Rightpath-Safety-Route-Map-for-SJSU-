import streamlit as st
import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt
import pickle
import pandas as pd

st.title("RightPath Safety Routing Demo")
st.write("Choose a routing mode and enter coordinates to compute a path.")

# --------------------------
# LOAD RIGHTPATH GRAPH + EDGES (Mac-compatible PKLs)
# --------------------------

st.write("Loading RightPath graph…")

G = None
edges_utm = None

try:
    with open("rightpath_graph_mac.pkl", "rb") as f:
        G = pickle.load(f)

    edges_utm = pd.read_pickle("rightpath_edges_mac.pkl")

    st.success("Graph and edges loaded successfully!")

except Exception as e:
    st.error("❌ Failed to load graph. Make sure the PKL files are in the same folder as app.py.")
    st.write(e)


# --------------------------
# ROUTING FUNCTIONS
# --------------------------

def nearest_node(G, lat, lon):
    return ox.distance.nearest_nodes(G, lon, lat)

def shortest_path(G, start_lat, start_lon, end_lat, end_lon):
    start = nearest_node(G, start_lat, start_lon)
    end = nearest_node(G, end_lat, end_lon)
    return nx.shortest_path(G, start, end, weight="length")

def safest_path(G, start_lat, start_lon, end_lat, end_lon):
    start = nearest_node(G, start_lat, start_lon)
    end = nearest_node(G, end_lat, end_lon)
    return nx.shortest_path(G, start, end, weight="safety_weight")

def hybrid_path(G, start_lat, start_lon, end_lat, end_lon):
    start = nearest_node(G, start_lat, start_lon)
    end = nearest_node(G, end_lat, end_lon)
    return nx.shortest_path(G, start, end, weight="hybrid_weight")


# --------------------------
# USER INPUT
# --------------------------

mode = st.selectbox(
    "Select Route Mode:",
    ["Shortest Path", "Safest Path", "Hybrid Path"]
)

st.subheader("Enter Start and End Coordinates:")

start_lat = st.number_input("Start Latitude", value=37.3353)
start_lon = st.number_input("Start Longitude", value=-121.8852)

end_lat = st.number_input("End Latitude", value=37.3338)
end_lon = st.number_input("End Longitude", value=-121.8810)


# --------------------------
# COMPUTE ROUTE
# --------------------------

if st.button("Compute Route"):
    if G is None:
        st.error("Graph not loaded yet!")
    else:
        st.write(f"Computing {mode}...")

        if mode == "Shortest Path":
            route = shortest_path(G, start_lat, start_lon, end_lat, end_lon)
        elif mode == "Safest Path":
            route = safest_path(G, start_lat, start_lon, end_lat, end_lon)
        else:
            route = hybrid_path(G, start_lat, start_lon, end_lat, end_lon)

        fig, ax = ox.plot_graph_route(
            G,
            route,
            route_linewidth=4,
            node_size=0,
            bgcolor="white",
            show=False,
            close=False
        )

        st.pyplot(fig)

        st.success(f"{mode} computed successfully!")
