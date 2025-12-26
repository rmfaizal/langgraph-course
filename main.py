from graph_intro_sample.flow import flow_sample
from graph_iterative_editor.iterative_editor import iterative_editor


def main():
    print("Hello from langgraph-course!")
    # LANGGRAPH FLOW SAMPLE
    flow_sample()
    # LANGGRAPH ITERATIVE EDITOR : review user input, critique, recommend, improve user input in an iterative graph loop
    iterative_editor()


if __name__ == "__main__":
    main()
