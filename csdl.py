import sqlite3

conn = sqlite3.connect("projectbcn.db")
cursor = conn.cursor()

# Bảng USER
cursor.execute("""
CREATE TABLE IF NOT EXISTS User (
    MSV TEXT PRIMARY KEY,
    name TEXT,
    age INTEGER,
    phone_number TEXT,
    email TEXT,
    khoa TEXT
);
""")

 #Bảng Tài liệu
cursor.execute("""
CREATE TABLE IF NOT EXISTS Tailieu (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    content TEXT
);
""")

# Bảng Tag
cursor.execute("""
CREATE TABLE IF NOT EXISTS Tag (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
);
""")

# Bảng Bài đăng
cursor.execute("""
CREATE TABLE IF NOT EXISTS Baidang (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    content TEXT,
    user_msv TEXT,
    FOREIGN KEY (user_msv) REFERENCES User(MSV)
);
""")

# Quan hệ: Tài liệu - Tag (nhiều-nhiều)
cursor.execute("""
CREATE TABLE IF NOT EXISTS Tailieu_Tag (
    tailieu_id INTEGER,
    tag_id INTEGER,
    FOREIGN KEY (tailieu_id) REFERENCES Tailieu(id),
    FOREIGN KEY (tag_id) REFERENCES Tag(id),
    PRIMARY KEY (tailieu_id, tag_id)
);
""")

# Quan hệ: User - Tài liệu (Tải về)
cursor.execute("""
CREATE TABLE IF NOT EXISTS Tai (
    user_msv TEXT,
    tailieu_id INTEGER,
    FOREIGN KEY (user_msv) REFERENCES User(MSV),
    FOREIGN KEY (tailieu_id) REFERENCES Tailieu(id),
    PRIMARY KEY (user_msv, tailieu_id)
);
""")

# Quan hệ: User - Tài liệu (Đánh giá)
cursor.execute("""
CREATE TABLE IF NOT EXISTS Danhgias (
    user_msv TEXT,
    tailieu_id INTEGER,
    rating INTEGER,
    FOREIGN KEY (user_msv) REFERENCES User(MSV),
    FOREIGN KEY (tailieu_id) REFERENCES Tailieu(id),
    PRIMARY KEY (user_msv, tailieu_id)
);
""")

# Quan hệ: User - Bài đăng (Lưu trữ)
cursor.execute("""
CREATE TABLE IF NOT EXISTS Luutru (
    user_msv TEXT,
    baidang_id INTEGER,
    FOREIGN KEY (user_msv) REFERENCES User(MSV),
    FOREIGN KEY (baidang_id) REFERENCES Baidang(id),
    PRIMARY KEY (user_msv, baidang_id)
);
""")

# Quan hệ: Bài đăng - Tag (nhiều-nhiều)
cursor.execute("""
CREATE TABLE IF NOT EXISTS Baidang_Tag (
    baidang_id INTEGER,
    tag_id INTEGER,
    FOREIGN KEY (baidang_id) REFERENCES Baidang(id),
    FOREIGN KEY (tag_id) REFERENCES Tag(id),
    PRIMARY KEY (baidang_id, tag_id)
);
""")
conn.commit()
conn.close()