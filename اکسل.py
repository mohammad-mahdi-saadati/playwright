import pandas as pd

file_path = "math.xlsx"
df = pd.read_excel(file_path, sheet_name="Sheet1")

def format_list_with_lessons(df_season, grade, season):
    """
    خروجی دو لیست (skills و lessons) برای یک فصل خاص
    """
    skills_lines = []
    lessons_lines = []

    for lesson_id in sorted(df_season["Lesson"].unique()):
        df_lesson = df_season[df_season["Lesson"] == lesson_id].sort_values("Order")

        # skills: تمام مهارت‌های این درس در یک خط
        skills_lines.append(f"    # درس {lesson_id}")
        skills_lines.append(
            "    " + ",".join([f'"{row.Name}"' for row in df_lesson.itertuples(index=False)]) + ","
        )

        # lessons: تمام تکرارهای این درس در یک خط
        lessons_lines.append(f"    # درس {lesson_id}: {len(df_lesson)} مهارت")
        lessons_lines.append(
            "    " + ",".join([f'"درس {lesson_id}"' for _ in df_lesson.itertuples(index=False)]) + ","
        )

    skills_str = (
        f"skills_math{grade}_chapter{season} = [\n" +
        "\n".join(skills_lines) +
        "\n]\n"
    )
    lessons_str = (
        f"lessons_math{grade}_chapter{season} = [\n" +
        "\n".join(lessons_lines) +
        "\n]\n"
    )
    return skills_str + lessons_str


# تست فقط پایه سوم
grade = 6
df_grade = df[df["Grade"] == grade]

for season in sorted(df_grade["Season"].unique()):
    df_season = df_grade[df_grade["Season"] == season]
    result = format_list_with_lessons(df_season, grade, season)
    print(result)
