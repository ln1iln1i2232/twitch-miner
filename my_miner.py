from TwitchChannelPointsMiner import TwitchChannelPointsMiner
from TwitchChannelPointsMiner.logger import LoggerSettings
from TwitchChannelPointsMiner.classes.entities.Streamer import Streamer
from TwitchChannelPointsMiner.classes.Settings import Priority

twitch_miner = TwitchChannelPointsMiner(
    username="ln1i",
    claim_drops_startup=False,
    priority=[
        Priority.STREAK,
        Priority.DROPS,
        Priority.ORDER
    ]
)

twitch_miner.mine(
    [
        Streamer("rnen"),
        Streamer("streamdatabase"),
        Streamer("badgearena"),
        Streamer("e4km"),
        Streamer("badgebybadge"),
        Streamer("igdy"),
    ],
    followers=False
