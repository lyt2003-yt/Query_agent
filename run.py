from langchain_core.messages import HumanMessage

from graph.state import QueryState
from graph.builder import build_graph

def test(query: str):
    state_data = {"source_question": query}
    initial_state = QueryState(**state_data)
    graph = build_graph()
    initial_state_dict = initial_state.model_dump()
    events = graph.stream(initial_state_dict)
    
    final_result = None  # 初始化 final_result，避免未赋值错误
    for event in events:
        print("<event>: ", event)
        if event.get("final_res"):
            final_result = event.get("final_res")

    return final_result

if __name__ == "__main__":
    question = input("请输入查询问题:")
    result = test(question)
    print("final result: ",result)