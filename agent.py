from crewai import Agent, Crew, Process, Task
from crewai_tools import PDFSearchTool
from crewai_tools import DirectorySearchTool
from dotenv import load_dotenv
import gc
gc.collect()

load_dotenv()

# --- Tools ---
pdf_search_tool = PDFSearchTool(
    pdf="pdf/curso-255606-aula-00-prof-diego-carvalho-e-fernando-pedrosa-8cf1-completo.pdf",
)
directory_search_tool = DirectorySearchTool(
    directory="./pdf",
)

# --- Agents ---
research_agent = Agent(
    role="Research Agent",
    goal="Search through the PDF to find relevant answers",
    allow_delegation=False,
    verbose=True,
    backstory=(
        """
        The research agent is adept at searching and 
        extracting data from documents, ensuring accurate and prompt responses.
        """
    ),
    tools=[pdf_search_tool],

)

# --- Tasks ---
answer_customer_question_task = Task(
    description=(
        """
        Answer the customer's questions based on the report PDF.
        The research agent will search through the PDF to find the relevant answers.
        Your final answer MUST be clear and accurate, based on the content of the PDF.

        Here is the customer's question:
        {customer_question}
        """
    ),
    expected_output="""
        Provide clear and accurate answers to the customer's questions based on 
        the content of the report PDF.
        """,
    tools=[pdf_search_tool],
    agent=research_agent,
)


# --- Crew ---
crew = Crew(
    agents=[research_agent],
    tasks=[answer_customer_question_task],
    process=Process.sequential,
)

# customer_question = input(
#     "qual a sua dúvida sobre o relatório?\n"
# )
# result = crew.kickoff(inputs={"customer_question": customer_question})
# print(result)
