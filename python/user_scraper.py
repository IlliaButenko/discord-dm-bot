import discum
TOKEN = "OTExNTk1NDk4MzE2NjQ0Mzgy.YZjrkw.tOsD7NoH_wy6e_QZlcHTkXJxWo4"
GUILDID = "961456809934200842"
CHANNELID = "961456809934200845"
bot = discum.Client(token=TOKEN)
def close_after_fetching(resp, guild_id):
    if bot.gateway.finishedMemberFetching(guild_id):
        lenmembersfetched = len(bot.gateway.session.guild(guild_id).members)
        print(str(lenmembersfetched) + ' members fetched')
        bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
        bot.gateway.close()


def get_members(guild_id, channel_id):
    bot.gateway.fetchMembers(guild_id, channel_id, wait=1)
    bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
    bot.gateway.run()
    bot.gateway.resetSession()
    return bot.gateway.session.guild(guild_id).members


members = get_members(GUILDID, CHANNELID)
for memberID in members:
    with open('users.csv', 'w') as f:
        for token in members:
            f.write(token)
            f.write("\n")

