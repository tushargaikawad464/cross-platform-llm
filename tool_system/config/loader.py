import yaml
import json
from pathlib import Path

def load_tools_config(file_path: Path) -> dict:
    """Load and validate YAML configuration"""
    with open(file_path) as f:
        raw_config = yaml.safe_load(f)
    
    tools = []

    print("Loading configuration:")

    # Add Tools
    # for tool in raw_config.get("tools", []):
    #     tool_name = tool.get("name")
    #     print(f"  Tool: {tool_name}")
    #     tools.append({
    #         tool_name: tool,
    #     })


    if not raw_config.get("tools", []):
        raise ValueError("No tools found in configuration.")
    for tool in raw_config.get("tools", []):
        data = generate_platform_schema("bedrock", tool)
        tools.append(data)
    
    print("Configuration loaded successfully.")
    print(json.dumps(tools[0], indent=2))
    return tools

def generate_platform_schema(platform: str, tool: dict) -> dict:
    print("""Generate platform-specific schema for the tool""")
    if platform == "OpenAIPlatform":
        return {
            'name': tool.get('name'),
            'type': 'function',
            'description': tool.get('description'),
            'parameters': {
                'type': 'object',
                'properties': tool.get('parameters', {}),
                'required': tool.get('required', [])
            }
        }
    elif platform == "BedrockPlatform":
        # Implement Bedrock schema generation
        return {
            'toolSpec': {
                'name': tool.get('name'),
                'description': tool.get('description'),
                'inputSchema': {
                    'json': {
                        'type': 'object',
                        'properties': tool.get('parameters', {}),
                        'required': tool.get('required', [])
                    }
                }
            }
        } 
    else:
        raise ValueError(f"Unsupported platform: {platform}")