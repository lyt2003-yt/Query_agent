from typing import Literal

# Define available LLM types
LLMType = Literal["basic","claude","embedding"]

# Define agent-LLM mapping
AGENT_LLM_MAP: dict[str, LLMType] = {
    "translator": "basic",
    "optant": "basic",
    "extractor": "basic",
    "reranker": "basic",
    "general_responder": "basic"
}



