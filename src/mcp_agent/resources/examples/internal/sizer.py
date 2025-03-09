import asyncio
from mcp_agent.core.fastagent import FastAgent

fast = FastAgent("Sizer Prompt Test")


@fast.agent("sizer", "given an object return its size", servers=["sizer"])
async def main():
    async with fast.run() as agent:
        await agent["sizer"].load_prompt("sizing_prompt")
        #        await agent("What is the size of the moon?")
        #        await agent("What is the size of the Earth?")
        #        await agent("What is the size of the Sun?")
        await agent()


if __name__ == "__main__":
    asyncio.run(main())
