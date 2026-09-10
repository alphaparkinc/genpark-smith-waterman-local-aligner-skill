import sys
import json
from client import SmithWaterman

def main():
    sw = SmithWaterman()
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        req = json.loads(line)
        method = req.get("method")
        params = req.get("params", {})
        if method == "align":
            score = sw.align(params.get("seq1", ""), params.get("seq2", ""))
            res = {"score": score}
        else:
            res = {"error": "unknown method"}
        sys.stdout.write(json.dumps({"id": req.get("id"), "result": res}) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
