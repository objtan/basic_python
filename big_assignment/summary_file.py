"""Tạo các màn hình giao diện dòng lệnh (CMD/Terminal):
	- Màn hình Menu chính: hiển thị danh sách các chức năng của chương trình
	- Màn hình Quản lý thông tin Học viên
	- Màn hình Quản lý thông tin Môn học
	- Màn hình Quản lý thông tin Điểm thi
"""

"""
+ Quản lý thông tin Học viên: Thêm/Sửa/Xoá/Tìm kiếm học viên theo Mã học viên, Họ tên, Email
"""

"""
+ Quản lý thông tin Môn học: Thêm/Sửa/Xoá/Tìm kiếm môn học theo Mã môn học, Tên môn học
"""

"""
+ Quản lý thông tin Điểm thi: Nhập điểm/Sửa điểm/Tra cứu điểm theo Mã học viên hoặc Họ tên học viên
/Thống kê danh sách các Học viên theo các mức Điểm tổng kết (A (90 <= điểm <= 100), B (70 <= điểm < 90), C (50 <= điểm < 70), D (điểm < 50)). 
Điểm tổng kết tình bằng công thức: Điểm tổng kết = (Điểm quá trình + Điểm kết thúc * 2) / 3
"""
'''
Kết xuất bảng điểm ra tệp tin export_data.json theo các tiêu chí: tất cả học viên; học viên điểm A; học viên điểm B; học viên điểm C; học viên điểm D. 
Thông tin kết xuất bao gồm: Mã học viên, Họ tên, Ngày sinh, Giới tính, Địa chỉ, Số điện thoại, Email, Tên môn học, Điểm quá trình, Điểm kết thúc, Điểm tổng kết
'''

# Do ID của student_id, subject_id là dạng ID custom nên em có tạo một số trigger trực tiếp ở MYSQL
'''
# Creating Trigger Python
    student_trigger_query=("""CREATE TRIGGER IF NOT EXISTS studtrigger 
                        BEFORE INSERT ON student 
                        FOR EACH ROW 
                        BEGIN 
                        INSERT INTO custom_student_id_table VALUES (NULL); 
                        SET NEW.Student_ID = CONCAT('PT', LPAD(LAST_INSERT_ID(), 4, '0')); 
                        END""")
    
    subject_trigger_query=("""CREATE TRIGGER IF NOT EXISTS subjtrigger
                BEFORE INSERT ON subject
                FOR EACH ROW
                BEGIN
                INSERT INTO custom_subject_id_table VALUES (NULL);
                SET NEW.Subject_ID = CONCAT('SJ', LPAD(LAST_INSERT_ID(), 3, '0'));
                END""")

'''
# tạo thêm 2 côt để tính điểm tổng kết và điểm (A, B, C, D, F)
'''         # add column PER_MARKS to the score table
            ALTER TABLE score ADD Per_Marks FLOAT

            # add column GRADE to the score table
            ALTER TABLE score ADD Grade VARCHAR(50)

            # Create trigger 
                        DELIMITER $$
                        CREATE TRIGGER scoretrigger 
                        BEFORE UPDATE ON score 
                        FOR EACH ROW 
                        BEGIN 
                        SET NEW.Per_Marks = (Midel_Score + Final_Score * 2)/3;
                        IF 9 <= NEW.Per_Marks AND NEW.Per_Marks <= 10 THEN
                        SET NEW.Grade = 'A';
                        ELSEIF 70 <= NEW.Per_Marks AND NEW.Per_Marks < 90 THEN
                        SET NEW.Grade = 'B';
                        ELSEIF 50 <= NEW.Per_Marks AND NEW.Per_Marks < 70 THEN
                        SET NEW.Grade = 'C';
                        ELSEIF NEW.Per_Marks <= 30 AND NEW.Per_Marks < 50 THEN
                        SET NEW.Grade = 'D';
                        ELSE SET NEW.Grade = 'F';
                        END IF;
                        END$$
                        DELIMITER ;

'''
