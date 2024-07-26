from firebase_config import db

def add_attendance(user_id, date, time, event_details):
    doc_ref = db.collection('attendance').document()
    doc_ref.set({
        'user_id': user_id,
        'date': date,
        'time': time,
        'event_details': event_details
    })

def get_attendance(user_id):
    attendance_ref = db.collection('attendance').where('user_id', '==', user_id)
    docs = attendance_ref.stream()
    attendance = []
    for doc in docs:
        attendance.append(doc.to_dict())
    return attendance
