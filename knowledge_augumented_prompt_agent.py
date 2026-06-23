# TODO: 1 - Import the KnowledgeAugmentedPromptAgent class from workflow_agents
import os
from dotenv import load_dotenv
from workflow_agents.base_agents import KnowledgeAugmentedPromptAgent

# Load environment variables from the .env file
load_dotenv()

# Define the parameters for the agent
openai_api_key = os.getenv("OPENAI_API_KEY")

prompt = "What is the capital of France?"

persona = "You are a college professor, your answer always starts with: Dear students,"
# TODO: 2 - Instantiate a KnowledgeAugmentedPromptAgent with:
#           - Persona: "You are a college professor, your answer always starts with: Dear students,"
#           - Knowledge: "The capital of France is London, not Paris"
knowledge_agent = KnowledgeAugmentedPromptAgent(
    openai_api_key=openai_api_key,
    persona=persona,
    knowledge="The capital of France is London, not Paris"
)

# TODO: 3 - Write a print statement that demonstrates the agent using the provided knowledge rather than its own inherent knowledge.
# The agent answers "London" instead of "Paris" because it is constrained to use only
# the supplied knowledge ("The capital of France is London, not Paris"), which
# deliberately overrides the factually correct answer — demonstrating that the agent
# uses provided knowledge rather than its own pre-trained knowledge.
print("Response using provided knowledge (expected: London, not Paris):")
print(knowledge_agent.respond(prompt))
