import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'),
              ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'),
              ('relev--ant', '-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]


def MED(S, T):
  # TO DO - modify to account for insertions, deletions and substitutions
  if (S == ""):
    return (len(T))
  elif (T == ""):
    return (len(S))
  else:
    if (S[0] == T[0]):
      return (MED(S[1:], T[1:]))
    else:
      return (1 + min(MED(S, T[1:]), MED(S[1:], T)))


def fast_MED(S, T, MED={}):
  # top-down memoization
  key = (S, T)
  if key not in MED:
    if (S == ""):
      MED[key] = len(T)
    elif (T == ""):
      MED[key] = len(S)
    else:
      if (S[0] == T[0]):
        MED[key] = fast_MED(S[1:], T[1:], MED)
      else:
        MED[key] = 1 + min(fast_MED(S, T[1:], MED), fast_MED(S[1:], T, MED))
  return MED[key]


def fast_align_MED(S, T, MED={}):
  key = (S, T)
  if key not in MED:
    if S == "":
      MED[key] = (len(T), "-" * len(T), T)
    elif T == "":
      MED[key] = (len(S), S, "-" * len(S))
    else:
      if S[0] == T[0]:
        dist, align_S, align_T = fast_align_MED(S[1:], T[1:], MED)
        MED[key] = (dist, S[0] + align_S, T[0] + align_T)
      else:
        dist1, align_S1, align_T1 = fast_align_MED(S, T[1:], MED)
        dist2, align_S2, align_T2 = fast_align_MED(S[1:], T, MED)
        if dist1 < dist2:
          MED[key] = (dist1 + 1, S[0] + align_S1, "-" + align_T1)
        else:
          MED[key] = (dist2 + 1, "-" + align_S2, T[0] + align_T2)
  return MED[key]


def test_MED():
  for S, T in test_cases:
    assert fast_MED(S, T) == MED(S, T)


def test_align():
  for i in range(len(test_cases)):
    S, T = test_cases[i]
    align_S, align_T = fast_align_MED(S, T)
    assert (align_S == alignments[i][0] and align_T == alignments[i][1])
