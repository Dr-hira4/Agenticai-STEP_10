from agents import Agent, Runner
from connection import config

agent = Agent(
    name = "Writer Agent",
    instructions = "You are a writer agent. Generate stories, poems, essay etc."
)

# Input and run agent
response = Runner.run_sync(
    agent,
    input = "Write a short essay on Quaid-e-Azam in simple English.",
    run_config = config
)

#Output
print(response)
