"""
ERES Semantic Spiral - Period-4 Cipher with the Carry Rule (dForm != dLineage)
Reference implementation + falsifiable test suite.  v0.2  (full canonical grid)

GRID SOURCE
-----------
ERES 3-Tier Semantics (JAS & Pi.ai, 29 Mar 2024, Open Source Creative Commons).
Loaded verbatim from the canonical source pair
(ERES3-TierSemantics.pdf + ERES_3-Tier_Semantics_Worksheet.docx).
Orders 1, 2, 4 are complete A-Z. Order 3 is complete except Z, which the source
leaves blank - carried as an HONEST GAP (a word needing Z at 3rd order RAISES;
it is never fabricated). L folds Pi.ai's "Love" into its anchor per source.

ASSIGNMENT (still PROPOSED, pending author's explicit yes)
----------------------------------------------------------
order 1 = JAS 1st-Order anchor
order 2 = JAS 2nd-Order
order 3 = JAS 3rd-Order
order 4 = Pi.ai 1st-Order virtue register  <-- the Signature / context-decider.
This last mapping is the one design choice Claude made; the engine is agnostic
to it (swap ORDER4 for any column and everything else holds).

THE CIPHER
----------
  order(p) = ((p-1) % 4) + 1        # position selects order, wrapping at four
  a TURN = one full four-step revolution.
  rung-4 of each turn = the SIGNATURE that DECIDES CONTEXT for that turn.

THE CARRY RULE  (dForm != dLineage, recursive)
----------------------------------------------
  the rung-4 Signature closing turn n seeds turn n+1. Form changes each turn;
  lineage does not. A later turn re-decides only as a DESCENDANT of what it
  inherited - an un-inherited (reset) context is INVALID. Drift is excluded.
"""

from dataclasses import dataclass

ORDER1 = {
    'A': 'About', 'B': 'Because', 'C': 'Christ', 'D': 'Devil', 'E': 'Evil',
    'F': 'Faith', 'G': 'God', 'H': 'Home', 'I': 'Image', 'J': 'Jesus',
    'K': 'Kingdom', 'L': 'Love (Family Amity)', 'M': 'Man', 'N': 'Nation',
    'O': 'Open', 'P': 'People', 'Q': 'Queen', 'R': 'Reason', 'S': 'Sacred',
    'T': 'Time', 'U': 'Uncle', 'V': 'Victory', 'W': 'Win', 'X': 'Xray',
    'Y': 'Yellow', 'Z': 'Zoo (Keepers)',
}
ORDER2 = {
    'A': 'Able', 'B': 'Better', 'C': 'Care', 'D': 'Double', 'E': 'Emit',
    'F': 'Free', 'G': 'Glass', 'H': 'Happy', 'I': 'Insert', 'J': 'Junior',
    'K': 'Keyword', 'L': 'Law', 'M': 'Meaning', 'N': 'Naughty', 'O': 'Often',
    'P': 'Place', 'Q': 'Quick', 'R': 'Ration', 'S': 'Suffer', 'T': 'Terrain',
    'U': 'Unplug', 'V': 'Vague', 'W': 'West', 'X': 'Xmas', 'Y': 'Yearly',
    'Z': 'Zipper',
}
ORDER3 = {
    'A': 'After', 'B': 'Belief', 'C': 'Curse', 'D': 'Duty', 'E': 'Effort',
    'F': 'Fruit', 'G': 'Green', 'H': 'Help', 'I': 'Income', 'J': 'Justice',
    'K': 'Knowledge', 'L': 'Learn', 'M': 'Marriage', 'N': 'Nobody',
    'O': 'Offshore', 'P': 'Police', 'Q': 'Question', 'R': 'Receipt',
    'S': 'Scholar', 'T': 'Tough', 'U': 'Upper', 'V': 'Vapor', 'W': 'Way',
    'X': 'Xtra', 'Y': 'Yearn',
    # 'Z' : intentionally absent - canonical source gap, not fabricated.
}
ORDER4 = {  # Pi.ai virtue register (PROPOSED context / Aura decider)
    'A': 'Awe', 'B': 'Belonging', 'C': 'Consciousness', 'D': 'Destiny',
    'E': 'Empathy', 'F': 'Flow', 'G': 'Growth', 'H': 'Harmony',
    'I': 'Introspection', 'J': 'Joy', 'K': 'Karma', 'L': 'Love',
    'M': 'Mindfulness', 'N': 'Nature', 'O': 'Openness', 'P': 'Purpose',
    'Q': 'Quest', 'R': 'Resilience', 'S': 'Synchronicity',
    'T': 'Transformation', 'U': 'Unity', 'V': 'Vision', 'W': 'Wonder',
    'X': 'Xenophilia', 'Y': 'Youthfulness', 'Z': 'Zenith',
}
GRID = {1: ORDER1, 2: ORDER2, 3: ORDER3, 4: ORDER4}


def order_of(position: int) -> int:
    if position < 1:
        raise ValueError("positions are 1-indexed")
    return ((position - 1) % 4) + 1


class MissingCell(KeyError):
    """A required (letter, order) cell is not in canon. We refuse to guess."""


def resolve_cell(letter: str, position: int) -> str:
    letter = letter.upper()
    o = order_of(position)
    table = GRID[o]
    if letter not in table:
        raise MissingCell(
            "order %d reading for %r not in canon (position %d)" % (o, letter, position)
        )
    return table[letter]


@dataclass
class Signature:
    turn: int
    position: int
    reading: str
    parent: object  # Signature | None

    def lineage(self):
        chain, s = [], self
        while s is not None:
            chain.append(s.reading)
            s = s.parent
        return list(reversed(chain))

    def is_inherited(self) -> bool:
        return self.turn == 1 or self.parent is not None


@dataclass
class Reading:
    word: str
    cells: list
    signatures: list


def cipher(word: str) -> Reading:
    word = word.strip().upper()
    cells, signatures, last_sig = [], [], None
    for i, letter in enumerate(word, start=1):
        o = order_of(i)
        reading = resolve_cell(letter, i)
        cells.append((i, letter, o, reading))
        if o == 4:
            sig = Signature(turn=i // 4, position=i, reading=reading, parent=last_sig)
            signatures.append(sig)
            last_sig = sig  # the Carry Rule: next turn inherits this
    return Reading(word=word, cells=cells, signatures=signatures)


def explain(word: str) -> str:
    r = cipher(word)
    out = ["%s   (period-4 cipher)" % word.upper()]
    for (p, letter, o, reading) in r.cells:
        mark = "   <- rung-4: SIGNATURE / decides context" if o == 4 else ""
        out.append("   p%-2d %s  order %d  =  %-16s%s" % (p, letter, o, reading, mark))
    if r.signatures:
        chain = r.signatures[-1].lineage()
        out.append("   Signature lineage: " + " -> ".join(chain))
        if len(chain) > 1:
            out.append("   (turn %d re-decided from inside the inheritance"
                       " - descent, not reset)" % r.signatures[-1].turn)
    else:
        out.append("   (no full four-step turn completed)")
    return "\n".join(out)


# --- Falsifiable test suite -------------------------------------------------
import unittest


class TestGridComplete(unittest.TestCase):
    def test_orders_1_2_4_full_AZ(self):
        AZ = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        for o in (1, 2, 4):
            self.assertEqual(set(GRID[o]), AZ, "order %d not full A-Z" % o)

    def test_order3_full_except_Z(self):
        AZ = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.assertEqual(set(GRID[3]), AZ - {'Z'})  # honest canon gap


class TestPeriod4(unittest.TestCase):
    def test_wrap(self):
        self.assertEqual([order_of(p) for p in range(1, 9)], [1, 2, 3, 4, 1, 2, 3, 4])


class TestArbitraryWords(unittest.TestCase):
    """The grid is now general - words outside the old CDEK-safe set cipher."""
    def test_signature(self):
        r = cipher("SIGNATURE")
        self.assertEqual([c[3] for c in r.cells],
                         ['Sacred', 'Insert', 'Green', 'Nature',
                          'About', 'Terrain', 'Upper', 'Resilience', 'Evil'])
        self.assertEqual(r.signatures[-1].lineage(), ['Nature', 'Resilience'])

    def test_provenance(self):
        r = cipher("PROVENANCE")
        self.assertEqual([(s.position, s.reading) for s in r.signatures],
                         [(4, 'Vision'), (8, 'Nature')])
        self.assertEqual(r.signatures[-1].lineage(), ['Vision', 'Nature'])


class TestCarryAndDrift(unittest.TestCase):
    def test_bedecked_two_signatures_descend(self):
        r = cipher("BEDECKED")
        s1, s2 = r.signatures
        self.assertIs(s2.parent, s1)
        self.assertEqual(s2.lineage(), ['Empathy', 'Destiny'])

    def test_uninherited_later_turn_is_invalid(self):
        self.assertFalse(Signature(2, 8, 'Destiny', None).is_inherited())


class TestNoFabrication(unittest.TestCase):
    def test_Z_third_order_gap_raises(self):
        # JAZZ: position 3 = Z at order 3 -> the one canonical gap -> must raise.
        with self.assertRaises(MissingCell):
            cipher("JAZZ")


class TestRegression(unittest.TestCase):
    def test_deeds(self):
        r = cipher("DEEDS")
        self.assertEqual([c[3] for c in r.cells],
                         ['Devil', 'Emit', 'Effort', 'Destiny', 'Sacred'])


if __name__ == "__main__":
    for w in ("DEEDS", "BEDECKED", "SIGNATURE", "PROVENANCE"):
        print("=" * 70)
        print(explain(w))
    print("=" * 70)
    print()
    unittest.main(verbosity=2)
