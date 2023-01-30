#include <vector>

std::vector<int> vertex_array;
std::vector<int> edge_array;
std::vector<int> row_pointer;

// Add vertices to the vertex array
for (int i = 0; i < num_vertices; i++) {
  vertex_array.push_back(i);
}

// Add edges to the edge array
for (int i = 0; i < num_edges; i++) {
  int start_vertex, end_vertex;
  // Read start_vertex and end_vertex for the i-th edge from input
  edge_array.push_back(start_vertex);
  edge_array.push_back(end_vertex);
}

// Initialize the row pointer array
row_pointer.resize(num_vertices + 1, 0);

// Fill the row pointer array
for (int i = 0; i < num_edges; i++) {
  int start_vertex = edge_array[2 * i];
  row_pointer[start_vertex + 1]++;
}

// Prefix sum to get the starting indices for each vertex
for (int i = 1; i < num_vertices + 1; i++) {
  row_pointer[i] += row_pointer[i - 1];
}
