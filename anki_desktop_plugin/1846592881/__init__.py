import anki.sync

# The '%s' in the strings is not used but the anki code requires it from >=2.1
anki.sync.SYNC_BASE = 'http://127.0.0.1:27701/%s'
anki.sync.SYNC_MEDIA_BASE = 'http://127.0.0.1:27701/msync/%s'
