def generate_report(results):
    print("\n===== TEST REPORT =====")

    for i, r in enumerate(results):
        if r is None:
            print(f"✘ UNKNOWN_TEST_{i} failed -> Test returned None")
            continue

        if not isinstance(r, dict):
            print(f"✘ UNKNOWN_TEST_{i} failed -> Invalid test result type: {type(r)}")
            continue

        if r.get("success", False):
            print(f"✔ {r.get('name', 'unknown')} passed")
        else:
            print(f"✘ {r.get('name', 'unknown')} failed -> {r.get('error', 'no error message')}")
