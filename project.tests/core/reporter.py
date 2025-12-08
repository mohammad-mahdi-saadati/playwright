def generate_report(results):
    print("\n===== TEST REPORT =====")

    for r in results:
        if r["success"]:
            print(f"✔ {r['name']} passed")
        else:
            print(f"✘ {r['name']} failed -> {r['error']}")
