# Simpan data peserta dalam list sementara
participants = []

def add_participant(username):
    if username not in participants:
        participants.append(username)

def get_participants():
    return participants
