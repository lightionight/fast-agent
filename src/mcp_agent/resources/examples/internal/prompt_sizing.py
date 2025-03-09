from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts.base import UserMessage, AssistantMessage

mcp = FastMCP("MCP Root Tester")


@mcp.prompt(name="sizing_prompt", description="set up the sizing protocol")
def sizing_prompt():
    return [
        UserMessage("What is the size of the moon?"),
        AssistantMessage("OBJECT: MOON\nSIZE: 3,474.8\nUNITS: KM\nTYPE: MINERAL"),
        UserMessage("What is the size of the Earth?"),
        AssistantMessage("OBJECT: EARTH\nSIZE: 12,742\nUNITS: KM\nTYPE: MINERAL"),
        UserMessage("A tiger"),
        AssistantMessage("OBJECT: TIGER\nSIZE: 1.2\nUNITS: M\nTYPE: ANIMAL"),
        UserMessage("Domestic Cat"),
    ]


if __name__ == "__main__":
    mcp.run()
