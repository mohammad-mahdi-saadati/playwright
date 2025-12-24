def generate_report(results):
    print("\n===== TEST REPORT =====")

    for r in results:
        if r.get("success", False):
            print(f"✔ {r['name']} passed")
        else:
            print(f"✘ {r['name']} failed -> {r.get('error')}")
