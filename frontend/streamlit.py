"""
streamlit run frontend/streamlit_app.py

Frontend starts at
http://localhost:8501
"""

import requests
import streamlit as st

# -----------------------------------------------------
# Page Config
# -----------------------------------------------------

st.set_page_config(
    page_title="🇮🇳 Bharat AI Trip Planner",
    page_icon="✈️",
    layout="wide"
)

# -----------------------------------------------------
# Header
# -----------------------------------------------------

st.title("🇮🇳 Bharat AI Trip Planner")

st.markdown(
    """
### Plan personalized trips across India using **Multi-Agent AI**

This application uses **LangGraph**, **Gemini**, **FastAPI**, **MCP**, and
**live Internet APIs** to generate intelligent travel itineraries.
"""
)

st.divider()

# -----------------------------------------------------
# Sidebar
# -----------------------------------------------------

st.sidebar.header("✈️ Trip Details")

source = st.sidebar.text_input(
    "Source",
    placeholder="Delhi"
)

destination = st.sidebar.text_input(
    "Destination",
    placeholder="Goa"
)

days = st.sidebar.number_input(
    "Number of Days",
    min_value=1,
    max_value=30,
    value=3
)

travellers = st.sidebar.number_input(
    "Number of Travellers",
    min_value=1,
    max_value=20,
    value=2
)

budget = st.sidebar.number_input(
    "Budget (₹)",
    min_value=1000,
    value=20000,
    step=1000
)

preferences = st.sidebar.text_area(
    "Preferences",
    placeholder="Beaches, food, adventure..."
)

plan_button = st.sidebar.button(
    "🚀 Generate Trip Plan",
    use_container_width=True
)

# -----------------------------------------------------
# Tabs
# -----------------------------------------------------

tab1, tab2, tab3 = st.tabs(
    [
        "✈️ Trip Planner",
        "🎯 Problem Statement",
        "🏗️ Architecture"
    ]
)

# =====================================================
# TAB 1
# =====================================================

with tab1:

    st.info(
        """
### 🧠 AI Powered Travel Planning

The system automatically:

- 🔍 Searches the Internet
- ☀️ Checks destination weather
- 🚆 Finds travel options
- 🏨 Recommends hotels
- 🗺️ Generates a day-wise itinerary
- 💰 Estimates total trip cost
- 🔁 Replans if the budget is exceeded
"""
    )

    if plan_button:

        if not source or not destination:

            st.error("Please enter both Source and Destination.")

        else:

            payload = {

                "source": source,
                "destination": destination,
                "days": days,
                "travellers": travellers,
                "budget": budget,
                "preferences": preferences

            }

            with st.spinner("Planning your trip..."):

                try:

                    response = requests.post(
                        "http://127.0.0.1:8000/plan-trip",
                        json=payload,
                        timeout=180
                    )

                    if response.status_code == 200:

                        result = response.json()

                        st.success("✅ Trip Plan Generated Successfully!")

                        col1, col2 = st.columns(2)

                        with col1:

                            st.metric(
                                "Estimated Cost",
                                f"₹{result['estimated_cost']}"
                            )

                        with col2:

                            if result["estimated_cost"] <= budget:

                                st.metric(
                                    "Budget Status",
                                    "✅ Within Budget"
                                )

                            else:

                                st.metric(
                                    "Budget Status",
                                    "⚠️ Over Budget"
                                )

                        st.divider()

                        st.markdown("## 🗺️ Personalized Trip Itinerary")

                        st.markdown(result["itinerary"])

                    else:

                        st.error(response.text)

                except Exception as ex:

                    st.error(str(ex))

    else:

        st.info(
            "Enter your trip details from the left panel and click **Generate Trip Plan**."
        )

# =====================================================
# TAB 2
# =====================================================

with tab2:

    st.header("🎯 Problem Statement")

    st.markdown(
        """
### 💡 Motivation

I enjoy travelling across India and **usually travel at least once every month**.

Whenever I plan a trip, I find myself opening multiple websites to collect information.

For every trip I typically need to search for:

- 🔍 Tourist attractions
- 🏨 Hotels
- ☀️ Weather
- 🚆 Travel routes
- 🍽️ Local food
- 💰 Budget estimation

Even for a short weekend trip, this planning process usually takes **1-2 days**.

I wanted to build a single AI application that could gather all this information from the internet and generate a complete travel plan automatically.
"""
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.error("❌ Traditional Trip Planning")

        st.markdown(
            """
- Open Google Search
- Read multiple blogs
- Check Google Maps
- Check Weather websites
- Search Hotels
- Estimate Budget manually
- Combine everything together
"""
        )

    with col2:

        st.success("✅ AI Powered Planning")

        st.markdown(
            """
Enter:

- Source
- Destination
- Number of Days
- Travellers
- Budget
- Preferences

↓

AI Agents collect live information

↓

Generate complete itinerary in seconds
"""
        )

    st.divider()

    st.subheader("🎯 Project Objectives")

    c1, c2 = st.columns(2)

    with c1:

        st.markdown(
            """
- ✅ Live Internet Search
- ✅ Weather Information
- ✅ Travel Suggestions
- ✅ Cost Estimation
"""
        )

    with c2:

        st.markdown(
            """
- ✅ Multi-Agent Workflow
- ✅ LangGraph
- ✅ FastAPI
- ✅ Streamlit
"""
        )

    st.divider()

    st.info(
        """
### 🎥 Demo Scenario

Suppose I want to travel:

**Delhi → Goa**

- 5 Days
- 2 Travellers
- Budget ₹25,000

Instead of opening multiple websites, I simply enter these details,
and the AI generates a personalized itinerary automatically.
"""
    )

# =====================================================
# TAB 3
# =====================================================

with tab3:

    st.header("🏗️ System Architecture")

    st.subheader("Overall Workflow")

    st.code(
"""
                    USER

                      │
                      ▼

               Streamlit UI

                      │
                      ▼

                 FastAPI API

                      │
                      ▼

                 LangGraph

                      │
                      ▼

              Planner Agent

                      │
                      ▼

             Tool Executor

        ┌─────────┼─────────┐

        ▼         ▼         ▼

    Search     Weather    Travel

        │         │         │

        └─────────┼─────────┘

                  ▼

            Tool Results

                  ▼

            Budget Agent

                  ▼

        Budget Validation
          |           | 
  (under budget)   (over budget) ─────   REPLAN ──────────────► Planner Agent
          |         
          │         
          ▼         
      Itinerary 
      Generator  (LLM)    
          |           
          |  
          ▼

         END   
"""
    )

    st.divider()

    st.subheader("⚙️ Agent Workflow")

    with st.expander("🧠 Planner Agent"):

        st.write(
            "Understands the user's request and decides which external tools are required."
        )

    with st.expander("🌐 Tool Executor"):

        st.write(
            "Executes Internet Search, Weather and Travel tools using MCP."
        )

    with st.expander("🗺️ Itinerary Generator"):

        st.write(
            "Uses Gemini LLM together with tool results to generate a personalized itinerary."
        )

    with st.expander("💰 Budget Agent"):

        st.write(
            "Estimates the overall trip cost and validates it against the user's budget."
        )

    with st.expander("🔁 Replan Agent"):

        st.write(
            "If the estimated cost exceeds the budget, a cheaper itinerary is generated."
        )

    st.divider()

    st.subheader("🛠️ Technology Stack")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.success("🖥️ Frontend\n\nStreamlit")

    with c2:
        st.success("⚡ Backend\n\nFastAPI")

    with c3:
        st.success("🧠 Workflow\n\nLangGraph")

    with c4:
        st.success("🤖 LLM\n\nGoogle Gemini")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.info("🔍 Search\n\nTavily API")

    with c2:
        st.info("☀️ Weather\n\nOpen-Meteo")

    with c3:
        st.info("🗺️ Travel\n\nGoogle Maps / Search")

    with c4:
        st.info("🐳 Deployment\n\nDocker")

    st.divider()

    st.subheader("🔌 APIs & Tools Used")

    st.markdown(
        """
- **Gemini API** – Itinerary generation and reasoning
- **Tavily API** – Live Internet search
- **Open-Meteo API** – Weather information
- **Google Maps / Search** – Travel suggestions
- **FastMCP** – Tool interface between agents and external APIs
"""
    )

    st.success(
        """
### Why LangGraph?

- Multi-Agent orchestration
- Shared state management
- Conditional workflow (Budget → Replan)
- Easy to extend with more agents
"""
    )

    st.info(
        """
### Why MCP?

Instead of allowing agents to directly call APIs,

Planner Agent

↓

MCP

↓

Search / Weather / Travel

This keeps the system modular and allows tools to be replaced without modifying the agents.
"""
    )

    st.divider()

    st.subheader("🚀 Future Improvements")

    st.checkbox("Flight Booking", disabled=True)
    st.checkbox("Hotel Booking", disabled=True)
    st.checkbox("Restaurant Recommendations", disabled=True)
    st.checkbox("Trip History", disabled=True)
    st.checkbox("Authentication", disabled=True)
    st.checkbox("Redis Cache", disabled=True)
    st.checkbox("Kubernetes Deployment", disabled=True)