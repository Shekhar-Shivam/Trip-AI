from backend.llm import llm_service

response = llm_service.invoke(
    """
    Suggest 3 places to visit in Jaipur.
    """
)

print(response)

# python test_llm.py