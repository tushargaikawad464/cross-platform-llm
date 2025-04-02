from pathlib import Path
from config.loader import load_tools_config
import yaml
# from .platforms import OpenAIPlatform, BedrockPlatform
# from .execution import HTTPExecutor


def main():
    # Load configuration
    tools = load_tools_config(Path("config/skills.yaml"))
    print("Loaded tools configuration:\n", yaml.dump(tools, indent=2))

    # # Setup platforms
    # platforms = {
    #     "openai": OpenAIPlatform(),
    #     "bedrock": BedrockPlatform()
    # }

if __name__ == "__main__":
    main()
