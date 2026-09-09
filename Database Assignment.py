import sqlite3

# 1. 데이터베이스 생성 및 연결 (없으면 새로 생성됨)
conn = sqlite3.connect('assignment.db')

with conn:
    cur = conn.cursor()
    # 2. AUTOINCREMENT 기본 키(ID)와 파일명(col_fname)을 저장할 테이블 생성
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT \
        )")
    conn.commit()

# 3. 테스트용 파일 이름 리스트 (교안에 맞게 수정하세요)
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.avi', 'World.txt', 'data.pdf', 'myPhoto.jpg')

# 4. for 루프를 사용해 리스트 안의 파일을 하나씩 검사
for file in fileList:
    # 5. 파일 이름이 '.txt'로 끝나는지 확인
    if file.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            # 6. DB에 데이터를 삽입. 이때 (file,)처럼 '단일 요소 튜플'을 사용해야 에러가 나지 않습니다.
            cur.execute("INSERT INTO tbl_files (col_fname) VALUES (?)", (file,))
            
            # 7. 요구 사항에 따라 자격을 갖춘 파일명을 콘솔에 출력
            print(f"데이터베이스에 성공적으로 추가된 텍스트 파일: {file}")

# 8. 모든 작업이 끝난 후 메모리 누수를 방지하기 위해 DB 연결 닫기
conn.close()