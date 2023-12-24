import firebase_admin
from firebase_admin import credentials, db

SETUP_PATH = './serviceAccountKey.json'
# Kiểm tra xem Firebase app đã được khởi tạo chưa
if not firebase_admin._apps:
    # Khởi tạo Firebase app nếu chưa tồn tại
    cred = credentials.Certificate(SETUP_PATH)
    firebase_admin.initialize_app(cred, {'databaseURL': 'https://lockpc-3d140-default-rtdb.asia-southeast1.firebasedatabase.app/'})
database=db