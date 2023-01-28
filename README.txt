Hello, i'm glad you to use my first program. I want to inprove my skills.

This program is supposed to monitor the relative price change of stack from OKX-website using telegram bot.
Pictures of charts will be created in a folder (you can change the root of the folder in config file).
In order to get started you need:
	-create a telegram bot;
	-fill in "config.py": token of bot and chat_id;
	-run "controller.py";
	-open telegram chat (using bot);
	-write "/start" to begin;

Menu:
Start monitoring - run monitoring;
Settings - open settings buttons to change settings;
	limit bars - set quantity of bars to view;
	time frame - choose time period (minutes, hours, days, e.t.);
	relative price change - set the number which is supposed to use for alert of price changing.
In order to stop monitoring you should press the button of start menu (Stop monitoring) or write "/stop".