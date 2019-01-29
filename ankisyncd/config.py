import configparser
import logging
import os
from os.path import dirname, realpath

paths = [
    "/etc/ankisyncd/ankisyncd.conf",
    os.environ.get("XDG_CONFIG_HOME") and
        (os.path.join(os.environ['XDG_CONFIG_HOME'], "ankisyncd", "ankisyncd.conf")) or
        os.path.join(os.path.expanduser("~"), ".config", "ankisyncd", "ankisyncd.conf"),
    os.path.join(dirname(dirname(realpath(__file__))), "ankisyncd.conf"),
]

# Get values from ENV and update the config. To use this prepend `ANKISYNCD_`
# to the uppercase form of the key. E.g, `ANKISYNCD_SESSION_MANAGER` to set
# `session_manager`
def load_from_env(conf):
    logging.info("Loading/overriding config values from ENV")
    for env in os.environ:
        if env.startswith('ANKISYNCD_'):
            config_key = env[10:].lower()
            conf[config_key] = os.getenv(env)
            logging.info(f"Setting {config_key} to {conf[config_key]} from ENV")

def load(path=None):
    choices = paths
    parser = configparser.ConfigParser()
    if path:
        choices = [path]
    for path in choices:
        logging.debug("config.location: trying", path)
        try:
            parser.read(path)
            conf = parser['sync_app']
            logging.info("Loaded config from {}".format(path))
            load_from_env(conf)
            return conf
        except KeyError:
            pass
    raise Exception("No config found, looked for {}".format(", ".join(choices)))
