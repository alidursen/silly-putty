from datetime import timedelta as td, datetime as dt

def ends_at(max_mana:float, percent_done:float)->float:
        """param:
        : max_mana: float, in terms of 1e14 mana
        : percent done: float, between 0 and 1
        """
        print(dt.now() + td(days=2e4/(24*36*max_mana)*(1-percent_done)))
