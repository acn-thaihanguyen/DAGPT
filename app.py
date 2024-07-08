from typing import Any, Dict, Optional

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from langchain.agents import AgentType
from langchain_openai import ChatOpenAI

from dagpt.agents.pandas_agent import DataAnalysisAgent
from dagpt.models.llms import load_llm
from dagpt.utils.utils import BaseLogger

# Load environment variables
load_dotenv()

logger = BaseLogger()


def execute_plot_code(code: str, df: pd.DataFrame) -> Optional[plt.Figure]:
    """Execute the plot code safely.

    Args:
        code (str): The code to execute.
        df (pd.DataFrame): The dataframe to use.

    Returns:
        fig: The matplotlib figure generated by the code.
    """
    try:
        local_vars = {"plt": plt, "df": df}
        compiled_code = compile(code, "<string>", "exec")
        exec(compiled_code, globals(), local_vars)
        return plt.gcf()
    except Exception as e:
        st.error(f"Error executing plot code: {e}")
        return None


def display_data(df: pd.DataFrame):
    """Display the dataframe in the Streamlit app."""
    st.write("### DataFrame Head:")
    st.write(df.head())


def get_agent_type() -> AgentType:
    """Get the agent type selected by the user."""
    return st.selectbox(
        "Select Agent Type",
        [AgentType.OPENAI_FUNCTIONS, AgentType.ZERO_SHOT_REACT_DESCRIPTION],
    )


def initialize_agent(
    df: pd.DataFrame, llm: ChatOpenAI, agent_type: AgentType, verbose: bool
) -> DataAnalysisAgent:
    """Initialize the Data Analysis Agent."""
    daagent = DataAnalysisAgent(
        df=df,
        llm=llm,
        agent_type=agent_type,
        verbose=verbose,
        return_intermediate_steps=True,
    )
    return daagent.create_agent()


def process_query(agent: DataAnalysisAgent, query: str):
    """Process the user query using the agent and display the response."""
    response = agent(query)
    st.session_state.history.append((query, response["output"]))

    if response["intermediate_steps"]:
        logger.info("### Intermediate steps ###")
        action = response["intermediate_steps"][-1][0].tool_input["query"]

        if "plt" in action:
            st.write(response["output"])
            fig = execute_plot_code(action, st.session_state.df)
            if fig:
                st.pyplot(fig)
            st.markdown("**Executed the code:**")
            st.code(action)
        else:
            st.write(response["output"])
    else:
        logger.info("### No intermediate steps ###")
        st.write(response["output"])


def display_chat_history():
    """Display the chat history."""
    st.markdown("### Chat History:")
    for i, (q, r) in enumerate(st.session_state.history):
        st.markdown(f"**Query {i+1}:** {q}")
        st.markdown(f"**Response {i+1}:** {r}")
        st.markdown("---")


def main():
    welcome_message = """
    Welcome to the Data Analysis Agent! 
    This tool allows you to upload your CSV data, ask questions about the data, and visualize the results.
    Get started by uploading your CSV file in the sidebar, then enter your query and let the agent do the rest!
    """
    st.title("Data Analysis Agent")
    st.caption(welcome_message)

    if "history" not in st.session_state:
        st.session_state.history = []

    llm = load_llm("gpt-3.5")

    with st.sidebar:
        uploaded_file = st.file_uploader("Upload your CSV here:", type="csv")

    if uploaded_file is not None:
        st.session_state.df = pd.read_csv(uploaded_file)
        display_data(st.session_state.df)
        agent_type = get_agent_type()
        verbose = False
        agent = initialize_agent(st.session_state.df, llm, agent_type, verbose)

        query = st.text_input("Enter your query:")

        if st.button("Run Query"):
            with st.spinner("Processing..."):
                process_query(agent, query)

        display_chat_history()


if __name__ == "__main__":
    main()