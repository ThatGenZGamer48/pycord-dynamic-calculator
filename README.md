# Pycord Dynamic Calculator

## Setup

Download and extract the zip file provided in [releases](https://github.com/ThatGenZGamer48/pycord-dynamic-calculator/releases) with your favourite file manager. 

## Editing Configuration File

Open the file and change the file name of `config.json.example` to `config.json`<br>
Then fill in the details below as such

1. Filling in Guild Ids
- First go to the discord server in which you want the bot's slash commands to register in,
- Then right click the Server Name and click Copy ID. ( If it doesn't show that option then try doing [this](https://techswift.org/2020/09/17/how-to-enable-developer-mode-in-discord/) )
- Go to the `config.json` file and locate `"guild_ids": [],`. Now fill in the copied thing inside `[]`.

2. Filling in the Token
- Create a bot in the discord developers page and copy the token
- Go to the `config.json` file and locate `"token": ""`. Now fill in the copied thing inside `""`. (`.env` files are better for storing bot tokens).

## Example Template

```json
{
    "guild_ids": [888888888888888888],
    "token": "XXXXXXXXXXXXXXXXXXXXXXXX.XXXXXX.XXXXXXXXXXXXXXXXXXXXXXXXXXX"
}
```

Then run the bot using `python src/main.py` in your terminal. 
