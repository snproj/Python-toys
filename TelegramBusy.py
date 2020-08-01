from telethon import TelegramClient, events
import datetime

api_id = XXXXXX
api_hash = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

client = TelegramClient('John Doe', api_id, api_hash)

################################################################

bridge_group_reply = """  -- No one's around to help --  

https://www.youtube.com/watch?v=yD2FSwTy2lw"""

################################################################

search_terms = ["john", "John", "JD", " jd "]

affected_groups = ["TestGroup1", "Bridge"]

affected_names = ["Jane"]

@client.on(events.NewMessage)
async def my_event_handler(event):
    now = datetime.datetime.now()
    current_chat = await event.get_chat()

    def log():
        print("AUTOREPLY AT: ")
        print(now.strftime("%Y-%m-%d, %H:%M:%S"))
        print(current_chat.title)
        print(current_chat)
        print("")

    print(current_chat)
    print(current_chat.first_name)

    #if current_chat.title in affected_groups:
        #for term in search_terms:
            #if term in event.raw_text:
                #await event.reply(bridge_group_reply)
                #await client.send_message("Jane", "test message")
                #log()
                #break

    if current_chat.first_name in affected_names:
        for term in search_terms:
            if term in event.raw_text:
                await event.reply(bridge_group_reply)
                #await client.send_message("Jane", "test message")
                log()
                break



client.start()
print("---------- AUTOREPLY ACTIVE ----------")
client.run_until_disconnected()
print("---------- DISCONNECTED ----------")