"""
ERES Semantic Spiral - Period-4 Cipher with the Carry Rule (dForm != dLineage)
Reference implementation + falsifiable test suite.  v0.1 PROPOSED / pre-canonical.

HONEST SCOPE
------------
- Order 1 (JAS 1st / anchor) and Order 4 (Pi.ai virtue register) are populated
  A-Z from canon.
- Orders 2 and 3 (JAS 2nd / 3rd) are PARTIAL - only the canonically-attested
  letters {C, D, E, K} are loaded. A missing cell RAISES; it is never
  fabricated (Data-Integrity: an absent reading is an error, not a guess).
- ORDER-4 = Pi.ai virtue column is a PROPOSED assignment (the aspirational /
  Aura register acting as the Signature / context-decider). Author confirm pending.

THE CIPHER
----------
  position selects order, wrapping at four:   order(p) = ((p-1) % 4) + 1
  a TURN = one full four-step revolution of the spiral.
  rung-4 (order 4) of each turn = the SIGNATURE that DECIDES CONTEXT for that turn.

THE CARRY RULE  (dForm != dLineage, recursive)
----------------------------------------------
  the rung-4 Signature closing turn n becomes the inherited context-seed of turn n+1.
  form changes each turn (new letters/orders); lineage does not.
  turn n+1 may re-decide context, but only as a DESCENDANT of the inherited
  Signature - an un-inherited (reset) context is an INVALID read.
  Drift is therefore structurally excluded, not merely discouraged.
"""

from dataclasses import dataclass

# --- Grid (canonical; partial where canon itself is partial) ----------------

ORDER1 = {  # JAS 1st-Order anchor
    'A': 'About', 'B': 'Because', 'C': 'Christ', 'D': 'Devil', 'E': 'Evil',
    'F': 'Faith', 'G': 'God', 'H': 'Home', 'I': 'Image', 'J': 'Jesus',
    'K': 'Kingdom', 'L': 'Love', 'M': 'Man', 'N': 'Nation', 'O': 'Open',
    'P': 'People', 'Q': 'Queen', 'R': 'Reason', 'S': 'Sacred', 'T': 'Time',
    'U': 'Uncle', 'V': 'Victory', 'W': 'Win', 'X': 'Xray', 'Y': 'Yellow',
    'Z': 'Zoo',
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
ORDER2 = {'C': 'Care', 'D': 'Double', 'E': 'Emit', 'K': 'Keyword'}     # PARTIAL
ORDER3 = {'C': 'Curse', 'D': 'Duty', 'E': 'Effort', 'K': 'Knowledge'}  # PARTIAL

GRID = {1: ORDER1, 2: ORDER2, 3: ORDER3, 4: ORDER4}


def order_of(position: int) -> int:
    """Period-4: position selects order, wrapping every four steps."""
    if position < 1:
        raise ValueError("positions are 1-indexed")
    return ((position - 1) % 4) + 1


class MissingCell(KeyError):
    """A required (letter, order) cell is not in the grid. We refuse to guess."""


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
    """A rung-4 context-decider. Its parent link IS its lineage."""
    turn: int
    position: int
    reading: str
    parent: object  # Signature | None

    def lineage(self):
        chain, s = [], self
        while s is not None:
            chain.append(s.reading)
            s = s.parent
        return list(reversed(chain))  # oldest -> newest

    def is_inherited(self) -> bool:
        # turn 1 legitimately seeds the chain; any later turn MUST inherit.
        return self.turn == 1 or self.parent is not None


@dataclass
class Reading:
    word: str
    cells: list       # [(position, letter, order, reading), ...]
    signatures: list  # [Signature, ...] one per completed turn


def cipher(word: str) -> Reading:
    word = word.strip().upper()
    cells, signatures, last_sig = [], [], None
    for i, letter in enumerate(word, start=1):
        o = order_of(i)
        reading = resolve_cell(letter, i)
        cells.append((i, letter, o, reading))
        if o == 4:  # rung-4 closes a turn -> mint a Signature carrying lineage
            turn = i // 4
            sig = Signature(turn=turn, position=i, reading=reading, parent=last_sig)
            signatures.append(sig)
            last_sig = sig  # <-- the Carry Rule: the next turn inherits this
    return Reading(word=word, cells=cells, signatures=signatures)


def explain(word: str) -> str:
    r = cipher(word)
    lines = ["%s   (period-4 cipher)" % word.upper()]
    for (p, letter, o, reading) in r.cells:
        mark = "   <- rung-4: SIGNATURE / decides context" if o == 4 else ""
        lines.append("   p%d  %s  order %d  =  %-14s%s" % (p, letter, o, reading, mark))
    if r.signatures:
        chain = r.signatures[-1].lineage()
        lines.append("   Signature lineage (oldest -> newest): " + " -> ".join(chain))
        if len(chain) > 1:
            lines.append("   (turn %d re-decided from inside the inheritance - "
                         "descent, not reset)" % r.signatures[-1].turn)
    else:
        lines.append("   (no full four-step turn completed)")
    return "\n".join(lines)


# --- Falsifiable test suite -------------------------------------------------

import unittest


class TestPeriod4(unittest.TestCase):
    def test_wrap(self):
        self.assertEqual([order_of(p) for p in range(1, 9)], [1, 2, 3, 4, 1, 2, 3, 4])


class TestBedecked(unittest.TestCase):
    """8 letters = TWO turns = TWO rung-4 Signatures. The residual case."""
    def setUp(self):
        self.r = cipher("BEDECKED")

    def test_eight_cells_resolve(self):
        self.assertEqual(
            [c[3] for c in self.r.cells],
            ['Because', 'Emit', 'Duty', 'Empathy',
             'Christ', 'Keyword', 'Effort', 'Destiny'],
        )

    def test_two_rung4_signatures(self):
        self.assertEqual(
            [(s.position, s.reading) for s in self.r.signatures],
            [(4, 'Empathy'), (8, 'Destiny')],
        )

    def test_second_signature_redecides_from_inheritance(self):
        s1, s2 = self.r.signatures
        self.assertIsNone(s1.parent)        # turn 1 seeds the chain
        self.assertIs(s2.parent, s1)        # turn 2 INHERITS turn 1
        self.assertEqual(s2.lineage(), ['Empathy', 'Destiny'])  # descent, not reset
        self.assertTrue(s2.is_inherited())


class TestDriftExcluded(unittest.TestCase):
    def test_uninherited_later_turn_is_invalid(self):
        orphan = Signature(turn=2, position=8, reading='Destiny', parent=None)
        self.assertFalse(orphan.is_inherited())  # a reset = an INVALID read


class TestNoFabrication(unittest.TestCase):
    def test_missing_cell_raises_not_fabricates(self):
        # position 2 = B, order 2; B has no loaded 2nd-order reading -> must raise.
        with self.assertRaises(MissingCell):
            cipher("ABBA")


class TestDeedsRegression(unittest.TestCase):
    """5 letters = one turn + one boundary (the earlier hand traversal)."""
    def test_deeds(self):
        r = cipher("DEEDS")
        self.assertEqual([c[3] for c in r.cells],
                         ['Devil', 'Emit', 'Effort', 'Destiny', 'Sacred'])
        self.assertEqual([(s.position, s.reading) for s in r.signatures],
                         [(4, 'Destiny')])


if __name__ == "__main__":
    print("=" * 68)
    print(explain("DEEDS"))
    print("-" * 68)
    print(explain("BEDECKED"))
    print("=" * 68)
    print()
    unittest.main(verbosity=2)
