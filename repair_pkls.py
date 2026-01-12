import pickle
import pandas as pd

print("Loading graph PKL...")
with open("rightpath_graph.pkl", "rb") as f:
    G = pickle.load(f)

print("Loading edges from CSV...")
edges_utm = pd.read_csv("edges_mac.csv")

print("Re-saving PKLs in Mac format...")

with open("rightpath_graph_mac.pkl", "wb") as f:
    pickle.dump(G, f)

edges_utm.to_pickle("rightpath_edges_mac.pkl")

print("✓ Done! Use rightpath_graph_mac.pkl and rightpath_edges_mac.pkl")
