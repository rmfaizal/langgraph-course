from graph_intro_sample.flow import flow_sample
from iterative_editor_reflection_agent.iterative_editor import iterative_editor
from reflexion_agent.reflexion_agent import reflexion_agent_invoke


def main():
    print("Hello from langgraph-course!")
    # LANGGRAPH FLOW SAMPLE
    flow_sample()
    # LANGGRAPH ITERATIVE EDITOR : review user input, critique, recommend, improve user input in an iterative graph loop
    iterative_editor()
    # LANGGRAPH REFLEXION AGENT : review user input, critique, recommend, improve user input in an iterative graph loop
    reflexion_agent_invoke()


if __name__ == "__main__":
    main()
