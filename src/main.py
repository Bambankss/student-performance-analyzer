from pathlib import Path
import pandas as pd
import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "student_performance.csv"
OUTPUT_DIR = PROJECT_ROOT / "outputs"
PASSING_SCORE = 60  # Batas latihan, bukan standar resmi institusi.


def load_data(path=DATA_PATH):
    """Baca CSV dan periksa kolom serta nilai yang diperlukan."""
    df = pd.read_csv(path)
    required_columns = {
        "student_id",
        "study_hours_per_week",
        "attendance_percent",
        "exam_score",
    }
    missing_columns = required_columns - set(df.columns)
    if missing_columns:
        raise ValueError(f"Kolom wajib tidak ditemukan: {sorted(missing_columns)}")

    numeric_columns = [
        "study_hours_per_week",
        "attendance_percent",
        "exam_score",
    ]
    for column in numeric_columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    df = df.dropna(subset=["student_id", *numeric_columns]).copy()

    if df.empty:
        raise ValueError("Tidak ada baris data valid setelah pemeriksaan.")

    if not df["attendance_percent"].between(0, 100).all():
        raise ValueError("attendance_percent harus berada pada rentang 0 sampai 100.")
    if not df["exam_score"].between(0, 100).all():
        raise ValueError("exam_score harus berada pada rentang 0 sampai 100.")
    if (df["study_hours_per_week"] < 0).any():
        raise ValueError("study_hours_per_week tidak boleh negatif.")

    return df


def descriptive_summary(df):
    """Hitung ringkasan statistik dasar."""
    return {
        "student_count": int(len(df)),
        "mean_score": float(df["exam_score"].mean()),
        "median_score": float(df["exam_score"].median()),
        "mean_study_hours": float(df["study_hours_per_week"].mean()),
        "mean_attendance": float(df["attendance_percent"].mean()),
        "below_threshold_count": int((df["exam_score"] < PASSING_SCORE).sum()),
        "at_or_above_threshold_count": int((df["exam_score"] >= PASSING_SCORE).sum()),
        "study_score_correlation": float(
            df["study_hours_per_week"].corr(df["exam_score"])
        ),
        "attendance_score_correlation": float(
            df["attendance_percent"].corr(df["exam_score"])
        ),
    }


def print_report(df, summary):
    """Tampilkan hasil analisis dan rekomendasi berbasis aturan."""
    print("\n=== STUDENT PERFORMANCE ANALYZER ===")
    print("Dataset: data contoh untuk pembelajaran")
    print(f"Jumlah mahasiswa dalam dataset : {summary['student_count']}")
    print(f"Rata-rata nilai ujian          : {summary['mean_score']:.2f}")
    print(f"Median nilai ujian             : {summary['median_score']:.2f}")
    print(f"Rata-rata waktu belajar        : {summary['mean_study_hours']:.2f} jam/minggu")
    print(f"Rata-rata kehadiran            : {summary['mean_attendance']:.2f}%")
    print(f"Nilai di bawah {PASSING_SCORE}             : {summary['below_threshold_count']}")
    print(f"Nilai >= {PASSING_SCORE}                    : {summary['at_or_above_threshold_count']}")
    print("\n--- Eksplorasi hubungan ---")
    print(f"Korelasi waktu belajar dengan nilai : {summary['study_score_correlation']:.2f}")
    print(f"Korelasi kehadiran dengan nilai     : {summary['attendance_score_correlation']:.2f}")
    print("Catatan: korelasi bukan bukti sebab-akibat.")

    below = df[df["exam_score"] < PASSING_SCORE]
    print("\n--- Rekomendasi awal ---")
    if below.empty:
        print("Tidak ada nilai di bawah batas latihan pada dataset ini.")
    else:
        print(
            f"Ada {len(below)} baris dengan nilai di bawah {PASSING_SCORE}. "
            "Tinjau kebutuhan dukungan belajar secara individual; jangan menyimpulkan "
            "penyebab hanya dari nilai."
        )

    if summary["study_score_correlation"] > 0.3:
        print(
            "Pada dataset ini, waktu belajar dan nilai menunjukkan hubungan positif "
            "yang cukup terlihat. Ini pola eksploratif, bukan bukti sebab-akibat."
        )
    elif summary["study_score_correlation"] < -0.3:
        print(
            "Pada dataset ini, waktu belajar dan nilai menunjukkan hubungan negatif "
            "yang cukup terlihat. Periksa kualitas data dan faktor lain sebelum menyimpulkan."
        )
    else:
        print(
            "Hubungan linear antara waktu belajar dan nilai tampak lemah pada dataset ini."
        )


def create_visualizations(df, output_dir=OUTPUT_DIR):
    """Simpan grafik hubungan waktu belajar dan nilai, serta distribusi nilai."""
    output_dir.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(8, 5))
    plt.scatter(df["study_hours_per_week"], df["exam_score"])
    plt.title("Waktu Belajar dan Nilai Ujian")
    plt.xlabel("Waktu belajar (jam per minggu)")
    plt.ylabel("Nilai ujian")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_dir / "study_hours_vs_score.png", dpi=150)
    plt.close()

    plt.figure(figsize=(8, 5))
    plt.hist(df["exam_score"], bins=6, edgecolor="black")
    plt.title("Distribusi Nilai Ujian")
    plt.xlabel("Nilai ujian")
    plt.ylabel("Jumlah mahasiswa")
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_dir / "score_distribution.png", dpi=150)
    plt.close()


def main():
    df = load_data()
    summary = descriptive_summary(df)
    print_report(df, summary)
    create_visualizations(df)
    print(f"\nGrafik disimpan di folder: {OUTPUT_DIR.relative_to(PROJECT_ROOT)}/")


if __name__ == "__main__":
    main()
