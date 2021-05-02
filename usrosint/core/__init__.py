from usrosint.modules.email import email
import json

class Core(object):

    from .menu import menu
    from .permutations import get_permutations
    from .results import print_results
    from .run import run
    from .report import generate_report, generate_json_report, generate_HTML_report
    from .modules import modules_update, get_report_modules
    from .logo import print_logo
    
    from .services.social import facebook, twitter, instagram, tiktok, pinterest, linktree, myspace
    from .services.forum import zeroxzerozerosec, jeuxvideo, hackernews, crackedto
    from .services.programming import github, pastebin, replit
    from .services.tchat import skype
    from .services.music import soundcloud, spotify
    from .services.entertainment import dailymotion, vimeo
    from .services.email import email
    from .services.porn import pornhub, redtube
    from .services.money import buymeacoffee
    from .services.domain import domain

    def __init__(self, config_path, items):
        self.version = "1.3.2"

        with open(config_path, 'r') as f:
            self.CONFIG = json.load(f)

        self.separators = []
        self.result = {}
        # Items passed from the command line
        self.items = items
        self.permutations_list = []
        self.modules = {
            # Emails
            "email":             {"method" : self.email },
            # Social
            "facebook":          {"method" : self.facebook},
            "twitter":           {"method" : self.twitter},
            "tiktok":            {"method" : self.tiktok},
            "instagram":         {"method" : self.instagram},
            "pinterest":         {"method" : self.pinterest},
            "linktree":          {"method" : self.linktree},
            "myspace":           {"method" : self.myspace},
            # Music
            "soundcloud":        {"method" : self.soundcloud},
            "spotify":           {"method" : self.spotify},
            # Programming 
            "github":            {"method" : self.github},
            "pastebin":          {"method" : self.pastebin},
            "replit":            {"method" : self.replit},
            # Forums:
            "0x00sec":           {"method" : self.zeroxzerozerosec},
            "jeuxvideo.com":     {"method" : self.jeuxvideo},
            "hackernews":        {"method" : self.hackernews},
            "crackedto":         {"method" : self.crackedto},
            # Tchat
            "skype":             {"method" : self.skype},
            # Entertainment
            "dailymotion":       {"method" : self.dailymotion},
            "vimeo":             {"method" : self.vimeo},   
            # Porn 
            "pornhub":           {"method" : self.pornhub},
            "redtube":           {"method" : self.redtube},
            # Money
            "buymeacoffee":      {"method" : self.buymeacoffee},
            # Domain
            "domain":            {"method" : self.domain}
        }