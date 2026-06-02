student_records = [
    {
        "student_id": "SV001",
        "name": "Nguyễn Văn A",
        "math": 8.5,
        "physics": 7.0,
        "chemistry": 9.0
    },
    {
        "student_id": "SV002",
        "name": "Trần Thị B",
        "math": 4.0,
        "physics": 5.5,
        "chemistry": 5.0
    },
    {
        "student_id": "SV003",
        "name": "Lê Văn C",
        "math": 9.5,
        "physics": 9.0,
        "chemistry": 8.5
    }
]


def calculate_average(student):
    return (student["math"] + student["physics"] + student["chemistry"]) / 3


def display_grades(records):
    if len(records) == 0:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    print("\n--- BẢNG ĐIỂM SINH VIÊN ---")

    for index, student in enumerate(records, start=1):
        avg = calculate_average(student)

        if avg >= 8:
            rank = "Giỏi"
        elif avg >= 6.5:
            rank = "Khá"
        elif avg >= 5:
            rank = "Trung bình"
        else:
            rank = "Yếu"

        print(f"{index}. [{student['student_id']}] " f"{student['name']} | " f"Toán: {student['math']} | " f"Lý: {student['physics']} | " f"Hóa: {student['chemistry']} | "f"ĐTB: {avg:.2f} - {rank}")

    print("---------------------------")


def update_student_score(records):
    student_id = input(
        "Nhập mã sinh viên cần cập nhật: "
    ).strip().upper()

    student_found = None

    for student in records:
        if student["student_id"] == student_id:
            student_found = student
            break

    if student_found is None:
        print(
            f"Không tìm thấy sinh viên mang mã "
            f"{student_id} trong hệ thống!"
        )
        return

    subject = input(
        "Chọn môn học (1-Toán, 2-Lý, 3-Hóa): "
    )

    if subject == "1":
        key = "math"
        subject_name = "Toán"
    elif subject == "2":
        key = "physics"
        subject_name = "Lý"
    elif subject == "3":
        key = "chemistry"
        subject_name = "Hóa"
    else:
        print("Môn học không hợp lệ!")
        return

    while True:
        try:
            new_score = float(input("Nhập điểm mới: "))

            if new_score < 0 or new_score > 10:
                print(
                    "Điểm số không hợp lệ. "
                    "Vui lòng nhập từ 0 đến 10!"
                )
                continue

            student_found[key] = new_score

            print(
                f">> Đã cập nhật điểm {subject_name} "
                f"của sinh viên "
                f"'{student_found['name']}' "
                f"thành {new_score}."
            )
            break

        except ValueError:
            print(
                "Điểm số không hợp lệ. "
                "Vui lòng nhập một số!"
            )


def generate_report(records):
    if len(records) == 0:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    total = len(records)
    passed = 0
    failed = 0

    for student in records:
        avg = calculate_average(student)

        if avg >= 5:
            passed += 1
        else:
            failed += 1

    pass_percent = (passed / total) * 100
    fail_percent = (failed / total) * 100

    print("\n--- BÁO CÁO HỌC VỤ ---")
    print(f"Tổng số sinh viên: {total}")
    print(
        f"Số lượng qua môn (ĐTB >= 5.0): "
        f"{passed} sinh viên "
        f"(Chiếm {pass_percent:.2f}%)"
    )
    print(
        f"Số lượng trượt (ĐTB < 5.0): "
        f"{failed} sinh viên "
        f"(Chiếm {fail_percent:.2f}%)"
    )
    print("----------------------")


def find_valedictorian(records):
    if len(records) == 0:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    top_student = records[0]
    highest_avg = calculate_average(records[0])

    for student in records:
        avg = calculate_average(student)

        if avg > highest_avg:
            highest_avg = avg
            top_student = student

    print("\n--- VINH DANH THỦ KHOA ---")
    print(
        f"Sinh viên: {top_student['name']} "
        f"(Mã: {top_student['student_id']})"
    )
    print(f"Điểm Trung Bình: {highest_avg:.2f}")
    print(
        "Chúc mừng sinh viên đã đạt "
        "thành tích xuất sắc nhất khóa!"
    )
    print("--------------------------")


def main():
    while True:
        print("""
===== HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI UNIVERSITY =====
1. Xem bảng điểm và học lực
2. Cập nhật điểm thi sinh viên
3. Báo cáo thống kê (Đỗ/Trượt)
4. Tìm sinh viên Thủ khoa
5. Thoát chương trình
======================================================
""")

        choice = input("Chọn chức năng (1-5): ")

        if choice == "1":
            display_grades(student_records)

        elif choice == "2":
            update_student_score(student_records)

        elif choice == "3":
            generate_report(student_records)

        elif choice == "4":
            find_valedictorian(student_records)

        elif choice == "5":
            print("Cảm ơn bạn đã sử dụng hệ thống!")
            break

        else:
            print("Lựa chọn không hợp lệ!")


main()