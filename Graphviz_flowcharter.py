from graphviz import Source

with open("flowchart_graph.dot", "r") as f:
    dot_content = f.read()

graph = Source(dot_content, format="png")

graph.render("flowchart_output", cleanup=True, renderer='cairo', formatter='cairo')
