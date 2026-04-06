from src.data_loader import load_dsa_data, load_jigsaw_data
from src.preprocessing import sample_data, filter_child_safety, create_toxicity_score
from src.analysis import platform_distribution, automation_rate
from src.visualization import plot_platform_distribution, plot_toxicity
from src.utils import find_column
from src.config import DSA_PATH, JIGSAW_PATH, OUTPUT_PATH, SAMPLE_SIZE


def main():
    print("\n==============================")
    print("  ONLINE SAFETY PROJECT START")
    print("==============================\n")

    # ─────────────────────────────────────────────────────────────
    # 1. LOAD DATA
    # ─────────────────────────────────────────────────────────────
    dsa = load_dsa_data(DSA_PATH)
    jigsaw = load_jigsaw_data(JIGSAW_PATH)

    if dsa is None:
        print("[FATAL] DSA data not loaded. Exiting...")
        return

    print(f"\n[DEBUG] DSA rows: {len(dsa):,}")
    if jigsaw is not None:
        print(f"[DEBUG] Jigsaw rows: {len(jigsaw):,}")
    else:
        print("[DEBUG] Jigsaw dataset not loaded")

    # ─────────────────────────────────────────────────────────────
    # 2. DETECT COLUMNS
    # ─────────────────────────────────────────────────────────────
    platform_col = find_column(dsa, ["platform"])
    category_col = find_column(dsa, ["category"])
    auto_col = find_column(dsa, ["automated"])

    print("\n[DEBUG] Detected columns:")
    print("Platform:", platform_col)
    print("Category:", category_col)
    print("Automated:", auto_col)

    # Check if critical columns exist
    if not platform_col:
        print("[ERROR] Platform column not found. Check dataset columns.")
        return

    if not auto_col:
        print("[WARNING] Automated column not found → skipping automation analysis")

    # ─────────────────────────────────────────────────────────────
    # 3. SAMPLE DATA (FOR PERFORMANCE)
    # ─────────────────────────────────────────────────────────────
    dsa = sample_data(dsa, SAMPLE_SIZE)

    print(f"[DEBUG] After sampling: {len(dsa):,} rows")

    # Preview data
    print("\n[DEBUG] Sample DSA data:")
    print(dsa.head(5))

    # ─────────────────────────────────────────────────────────────
    # 4. ANALYSIS
    # ─────────────────────────────────────────────────────────────
    print("\n==============================")
    print("  ANALYSIS RESULTS")
    print("==============================")

    # Platform distribution
    platform_counts = platform_distribution(dsa, platform_col)
    if platform_counts is not None:
        print("\n=== PLATFORM DISTRIBUTION ===")
        print(platform_counts.head(10))
    else:
        print("[ERROR] Platform distribution failed")

    # Automation rate
    if auto_col:
        automation = automation_rate(dsa, platform_col, auto_col)
        if automation is not None:
            print("\n=== AUTOMATION RATE (%) ===")
            print(automation.head(10))
        else:
            print("[ERROR] Automation analysis failed")

    # ─────────────────────────────────────────────────────────────
    # 5. VISUALIZATION
    # ─────────────────────────────────────────────────────────────
    print("\n[INFO] Generating visualizations...")

    try:
        plot_platform_distribution(platform_counts, OUTPUT_PATH)
        print("[SUCCESS] Platform distribution plot saved")
    except Exception as e:
        print(f"[ERROR] Plot failed: {e}")

    # ─────────────────────────────────────────────────────────────
    # 6. JIGSAW ANALYSIS
    # ─────────────────────────────────────────────────────────────
    if jigsaw is not None:
        print("\n==============================")
        print("  JIGSAW ANALYSIS")
        print("==============================")

        try:
            jigsaw = create_toxicity_score(jigsaw)

            print("\n[DEBUG] Jigsaw sample:")
            print(jigsaw.head(5))

            print("\n=== TOXICITY DISTRIBUTION ===")
            print(jigsaw["toxicity_score"].value_counts().head())

            plot_toxicity(jigsaw, OUTPUT_PATH)
            print("[SUCCESS] Toxicity plot saved")

        except Exception as e:
            print(f"[ERROR] Jigsaw processing failed: {e}")

    # ─────────────────────────────────────────────────────────────
    # 7. CHILD SAFETY FILTER (OPTIONAL)
    # ─────────────────────────────────────────────────────────────
    if category_col:
        try:
            child_df = filter_child_safety(dsa, category_col)

            if child_df is not None:
                print("\n=== CHILD SAFETY DATA ===")
                print(f"Total records: {len(child_df):,}")
                print(child_df.head(5))
        except Exception as e:
            print(f"[ERROR] Child safety analysis failed: {e}")

    # ─────────────────────────────────────────────────────────────
    # DONE
    # ─────────────────────────────────────────────────────────────
    print("\n==============================")
    print("  PROJECT COMPLETED")
    print("==============================")
    print(f"\n👉 Check 'outputs/' folder for results\n")


if __name__ == "__main__":
    main()