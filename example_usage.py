from client import SmithWaterman

def main():
    print("=== Testing Smith-Waterman Local Aligner ===")
    sw = SmithWaterman(match=2, mismatch=-1, gap=-1)
    s1 = "ACACACTA"
    s2 = "AGCACACA"
    score = sw.align(s1, s2)
    print(f"Local alignment score: {score}")

    assert score >= 10
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
