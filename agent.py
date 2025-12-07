from langgraph.graph import StateGraph, START, END
from hello import portfoliostate, cal_total, cal_total_inr, cal_total_eur, choose_conversion
from IPython.display import display, Image
from pathlib import Path

builder = StateGraph(portfoliostate)
builder.add_node("cal_total", cal_total)
builder.add_node("cal_total_inr", cal_total_inr)
builder.add_node("cal_total_eur", cal_total_eur)


builder.add_edge(START,"cal_total")
builder.add_conditional_edges(
    "cal_total",  
    choose_conversion,
    {
        "INR": "cal_total_inr",
        "EUR": "cal_total_eur",
    }
    )
builder.add_edge({"cal_total_inr","cal_total_eur"},END)

graph = builder.compile()
# display(Image(graph.get_graph().draw_mermaid_png()))

input_state = portfoliostate(amount_usd=100,target_currency='INR')
result = graph.invoke(input_state)
print(result)
print("-------------GRAPH--------------")
print(graph.get_graph().draw_mermaid())




png_bytes = graph.get_graph().draw_mermaid_png()

file_path = Path("portfolio_graph.png")
with open(file_path, "wb") as f:
    f.write(png_bytes)

print(f"\n✅ Graph saved as PNG at: {file_path.resolve()}")

