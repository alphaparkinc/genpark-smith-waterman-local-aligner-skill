class SmithWaterman:
    """
    Smith-Waterman Local Sequence Alignment Algorithm.
    Identifies high-scoring local motif alignments.
    """
    def __init__(self, match=2, mismatch=-1, gap=-1):
        self.match = match
        self.mismatch = mismatch
        self.gap = gap

    def align(self, s1, s2):
        n = len(s1)
        m = len(s2)
        score = [[0] * (m + 1) for _ in range(n + 1)]
        max_score = 0

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                match_score = self.match if s1[i - 1] == s2[j - 1] else self.mismatch
                score[i][j] = max(
                    0,
                    score[i - 1][j - 1] + match_score,
                    score[i - 1][j] + self.gap,
                    score[i][j - 1] + self.gap
                )
                if score[i][j] > max_score:
                    max_score = score[i][j]
        return max_score
