import signal
import sys
from fastmcp import FastMCP

mcp = FastMCP("Simple Demo Server")


@mcp.tool()
def tool_1() -> str:
    """Tool 1 - NOW THE NAME HAS CHANGED!!"""
    return "tool_1"


@mcp.tool()
def tool_2() -> str:
    """Tool 2 - returns its name"""
    return "tool_2"


@mcp.tool()
def tool_3() -> str:
    """Tool 3 - returns its name"""
    return "tool_3"


@mcp.tool()
def tool_4() -> str:
    """Tool 4 - returns its name"""
    return "tool_4"


@mcp.tool()
def tool_5() -> str:
    """Tool 5 - returns its name"""
    return "tool_5"


@mcp.tool()
def tool_6() -> str:
    """Tool 6 - returns its name"""
    return "tool_6"


@mcp.tool()
def tool_7() -> str:
    """Tool 7 - returns its name"""
    return "tool_7"


@mcp.tool()
def tool_8() -> str:
    """Tool 8 - returns its name"""
    return "tool_8"


@mcp.tool()
def tool_9() -> str:
    """Tool 9 - returns its name"""
    return "tool_9"


@mcp.tool()
def tool_10() -> str:
    """Tool 10 - returns its name"""
    return "tool_10"


@mcp.tool()
def tool_11() -> str:
    """Tool 11 - returns its name"""
    return "tool_11"


@mcp.tool()
def tool_12() -> str:
    """Tool 12 - returns its name"""
    return "tool_12"


@mcp.tool()
def tool_13() -> str:
    """Tool 13 - returns its name"""
    return "tool_13"


@mcp.tool()
def tool_14() -> str:
    """Tool 14 - returns its name"""
    return "tool_14"


@mcp.tool()
def tool_15() -> str:
    """Tool 15 - returns its name"""
    return "tool_15"


def signal_handler(signum, frame):
    """Handle graceful shutdown"""
    print("\nShutting down gracefully...")
    sys.exit(0)


if __name__ == "__main__":
    # Register signal handlers for graceful shutdown
    signal.signal(signal.SIGINT, signal_handler)  # Ctrl+C
    signal.signal(signal.SIGTERM, signal_handler)  # kill command

    try:
        mcp.run(transport="http")
    except KeyboardInterrupt:
        print("\nShutting down gracefully...")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
