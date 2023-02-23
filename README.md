# date-discord-bot
Simple discord bot to convert English(AD) to Nepali(BS) date.

## Commands
The bot has two slash commands.
- `/help` for help. 
- `/date` to convert todays date. 
- `/date <today|yesterday|tommorrow|yyyy-mm-dd>` to specify date. 
 
## Credits
Parses date using hamro patro date converter api. <br/>
Hamro Patro Date Converter: https://www.hamropatro.com/date-converter

## Invite the bot to your server.
Use this link: <a href="https://discord.com/api/oauth2/authorize?client_id=1078326907780735057&permissions=274877910016&scope=bot%20applications.commands" target="_blank">Link</a>

## Run the bot yourself
1. Create a .env file at project root with following contents.
```
BOT_TOKEN=<Your Discord Bot Token>
```
2. Run the bot
```
python main.py
```

