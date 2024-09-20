# Algokit assignment complete

I DID THE THING??

https://lora.algokit.io/testnet/application/722424786

## A few notes:
- I spent about two hours getting to the point of testing it on localnet; I pretty much just fixed all the error messages and my gut tells me there's a better way to write what I have written; I'm not used to types in Python.
- Half of that was figuring out how to pass the transaction parameters because I didn't find anything that explicitly stated I'd need to change that in the deploy file.
- At this point my questions would have revolved around setting the up accounts to work with the testnet - how to change the wallet and account from whatever the default was.
- I was having fun and refused to be defeated so close to the finish line so I finished it anyway.

## Questions/further investigation:
- How does the wallet and account work? There seemed to be two separate ID numbers and I don't actually know where the non-wallet one comes from.
- I have no idea how to edit the deploy file to call the application (as per the instructions) there instead of the command line, so would need to figure that out.
- How can I refund the rest of the tokens? I have readded the connection in Defly and it's still not letting me refund.
- What are the tradeoffs for using Beaker? I had intially tried that because I found an example in one of Algorand's articles, but then changed it because we're supposed to use Puya.
- How can I verify the data's been put into the box successfully before I deploy? Or that the box isn't empty? Better yet - how would something like this be done with larger data sets?

Ah, well. That was interesting.

--------------------------------------------------------------------------------

# algo-tutorial

Welcome to your new AlgoKit project!

This is your workspace root. A `workspace` in AlgoKit is an orchestrated collection of standalone projects (backends, smart contracts, frontend apps and etc).

By default, `projects_root_path` parameter is set to `projects`. Which instructs AlgoKit CLI to create a new directory under `projects` directory when new project is instantiated via `algokit init` at the root of the workspace.

## Getting Started

To get started refer to `README.md` files in respective sub-projects in the `projects` directory.

To learn more about algokit, visit [documentation](https://github.com/algorandfoundation/algokit-cli/blob/main/docs/algokit.md).

### GitHub Codespaces

To get started execute:

1. `algokit generate devcontainer` - invoking this command from the root of this repository will create a `devcontainer.json` file with all the configuration needed to run this project in a GitHub codespace. [Run the repository inside a codespace](https://docs.github.com/en/codespaces/getting-started/quickstart) to get started.
2. `algokit init` - invoke this command inside a github codespace to launch an interactive wizard to guide you through the process of creating a new AlgoKit project

Powered by [Copier templates](https://copier.readthedocs.io/en/stable/).
